import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        Art[] arts = new Art[n];
        for (int i = 0; i < n; i++) {
            arts[i] = new Art(sc.nextLong(), sc.nextInt());
        }
        Arrays.sort(arts);
        long[] values = new long[n + 1];
        long max = Long.MIN_VALUE;
        long min = Long.MAX_VALUE;
        for (int i = 1; i <= n; i++) {
            values[i] = arts[i - 1].value + values[i - 1];
            min = Math.min(min, values[i - 1] - arts[i - 1].size);
            max = Math.max(max, values[i] - arts[i - 1].size - min);
        }
        System.out.println(max);
    }
    
    static class Art implements Comparable<Art> {
        long size;
        int value;
        
        public Art(long size, int value) {
            this.size = size;
            this.value = value;
        }
        
        public int compareTo(Art another) {
            if (size == another.size) {
                return 0;
            } else if (size < another.size) {
                return -1;
            } else {
                return 1;
            }
        }
    }
}
