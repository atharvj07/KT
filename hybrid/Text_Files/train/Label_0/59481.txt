import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        TreeSet<Num> front = new TreeSet<>();
        TreeSet<Num> frontStock = new TreeSet<>();
        long frontSum = 0;
        TreeSet<Num> back = new TreeSet<>();
        long backSum = 0;
        Num[] arr = new Num[3 * n];
        for (int i = 0; i < 2 * n; i++) {
            arr[i] = new Num(i, sc.nextInt());
            frontSum += arr[i].value;
            front.add(arr[i]);
        }
        for (int i = 0; i < n; i++) {
            Num tmp = front.pollFirst();
            frontSum -= tmp.value;
            frontStock.add(tmp);
        }
        for (int i = 2 * n; i < 3 * n; i++) {
            arr[i] = new Num(i, sc.nextInt());
            backSum += arr[i].value;
            back.add(arr[i]);
        }
        long max = frontSum - backSum;
        for (int i = n * 2 - 1; i >= n; i--) {
            if (front.contains(arr[i])) {
                front.remove(arr[i]);
                frontSum -= arr[i].value;
                Num tmp = frontStock.pollLast();
                front.add(tmp);
                frontSum += tmp.value;
            } else {
                frontStock.remove(arr[i]);
            }
            back.add(arr[i]);
            backSum += arr[i].value;
            Num tmp = back.pollLast();
            backSum -= tmp.value;
            max = Math.max(max, frontSum - backSum);
        }
        System.out.println(max);
    }
    
    static class Num implements Comparable<Num> {
        int idx;
        int value;
        
        public Num(int idx, int value) {
            this.idx = idx;
            this.value = value;
        }
        
        public int hashCode() {
            return idx;
        }
        
        public boolean equals(Object o) {
            Num n = (Num)o;
            return idx == n.idx;
        }
        
        public int compareTo(Num another) {
            if (value == another.value) {
                return idx - another.idx;
            } else {
                return value - another.value;
            }
        }
        
        public String toString() {
            return idx + ":" + value;
        }
    }
}