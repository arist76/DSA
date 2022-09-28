int countingValleys(int steps, string path) {
    int hicker = 0;
    unsigned int valley_counter = 0;
    for (unsigned int i = 0; i < steps; i++)
    {
        int prev_hicker = hicker;
        if (path[i] == 'U')
            hicker++;
        else if (path[i] == 'D')
            hicker--;
            
        if (hicker == 0 && prev_hicker < 0)
            valley_counter++;
    }
    return valley_counter;
}
