#include <stdio.h>
#include <stdlib.h>
#include <pthread.h>
#include <unistd.h>
#include <time.h>

// Global Mutex to prevent race conditions on the standard output
// pthread_mutex_t is the POSIX threads (pthreads) data type used for mutual exclusion,
pthread_mutex_t console_mutex;

// Thread 1: Temperature Sensor Simulator
void *read_temperature(void *arg)
{
    while (1)
    {
        // Generate random temperature between 20 and 30
        int temp = 20 + rand() % 11;

        // Lock the mutex before writing to the shared resource (stdout)
        pthread_mutex_lock(&console_mutex);

        printf("TEMP,%d\n", temp);
        fflush(stdout); // CRITICAL: Force the buffer to flush immediately for IPC

        pthread_mutex_unlock(&console_mutex); // Unlock the mutex

        sleep(1); // Wait 1 second
    }
    return NULL;
}

// Thread 2: Humidity Sensor Simulator
void *read_humidity(void *arg)
{
    while (1)
    {
        // Generate random humidity between 40 and 60
        int hum = 40 + rand() % 21;

        // Lock the mutex
        pthread_mutex_lock(&console_mutex);

        printf("HUM,%d\n", hum);
        fflush(stdout); // CRITICAL: Force the buffer to flush immediately for IPC

        pthread_mutex_unlock(&console_mutex); // Unlock the mutex

        sleep(2); // Wait 2 seconds (different frequency to show asynchrony)
    }
    return NULL;
}

int main()
{
    // Initialize the random number generator seed
    srand(time(NULL));

    // Initialize the mutex
    if (pthread_mutex_init(&console_mutex, NULL) != 0)
    {
        perror("Mutex init failed");
        return 1;
    }

    // Declare thread identifiers
    pthread_t temp_thread, hum_thread;

    // Create the threads (spawning the sensors)
    pthread_create(&temp_thread, NULL, read_temperature, NULL);
    pthread_create(&hum_thread, NULL, read_humidity, NULL);

    // Wait for threads to finish (in this infinite loop, they won't)
    pthread_join(temp_thread, NULL);
    pthread_join(hum_thread, NULL);

    // Destroy the mutex (Good practice, even if unreachable here)
    pthread_mutex_destroy(&console_mutex);

    return 0;
}