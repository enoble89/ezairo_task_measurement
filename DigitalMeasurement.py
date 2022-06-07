# import math
import numpy as np

from saleae.range_measurements import DigitalMeasurer

tasks = [
        'signal_path',
        'signal_path_bypass',
        'freq_shift',
        'aux_out',
        'fbm_update',
        'compressor',
        'tnr',
        'sig_gen',
        'mpo',
        'virtual_fb',
        'fbm',
        'mlnr',
        'volume'
]

class MyDigitalMeasurer(DigitalMeasurer):
    supported_measurements = tasks

    # Initialize your measurement extension here
    # Each measurement object will only be used once, so feel free to do all per-measurement initialization here
    def __init__(self, requested_measurements):
        super().__init__(requested_measurements)
        self.pulse_count = 0
        self.last_state = None
        self.last_time = None
        self.task_id_pulse_threshold_secs = 120e-9
        self.task_runtime_data = np.zeros(len(tasks))

    # This method will be called one or more times per measurement with batches of data
    # data has the following interface
    #   * Iterate over to get transitions in the form of pairs of `Time`, Bitstate (`True` for high, `False` for low)
    # `Time` currently only allows taking a difference with another `Time`, to produce a `float` number of seconds
    def process_data(self, data):
        for t, bitstate in data:
            if self.last_state is None:
                self.last_state = bitstate
                self.last_time = t
                continue
            
            time_delta = float(t - self.last_time)
            self.last_time = t
            
            # Low to High transition
            if self.last_state and not bitstate:
                if time_delta < self.task_id_pulse_threshold_secs:
                    self.pulse_count += 1
                else:
                    self.task_runtime_data[self.pulse_count - 1] += time_delta 
                    self.pulse_count = 0


    # This method is called after all the relevant data has been passed to `process_data`
    # It returns a dictionary of the request_measurements values
    def measure(self):
        values = {}
        for i, task_name in enumerate(tasks):
            values[task_name] = self.task_runtime_data[i]
        return values
