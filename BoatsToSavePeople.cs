public class Solution {
    public int NumRescueBoats(int[] people, int limit) {
        int boats = 0;
        int end = people.Length - 1;
        Array.Sort(people);
        Array.Reverse(people);
        int temp;
        for (int i = 0; i <= end; i++) {
            if (i == end) {
                boats++;
                break;
            }
            if (people[i] + people[end] <= limit) {
                end--;
            }
            boats++;
        }
        return boats;
    }
}