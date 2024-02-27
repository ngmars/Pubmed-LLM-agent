from multiprocessing import Pool
from data_extraction_converted import abstract_data_main_function

if __name__ == '__main__':
    # Define the range of 'i' values
    i_values = list(range(8, 51))  

    # Set the number of processes to be used
    num_processes = 64  # You can adjust this number based on your system capabilities

    pool =  Pool(processes=num_processes)
        # Distribute the workload across processes
    
    async_results = pool.map_async(abstract_data_main_function, i_values)
    async_results.get()