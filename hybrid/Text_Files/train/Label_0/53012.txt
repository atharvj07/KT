import java.util.ArrayList;
import java.util.Scanner;
import java.util.TreeSet;

public class Main {
  static Scanner sc = new Scanner(System.in);

  public static void main(String[] args) {
    int N = sc.nextInt();
    int Q = sc.nextInt();
    int[] A = new int[Q];
    long[] B = new long[Q];
    for (int i = 0; i < Q; i++) {
      A[i] = Integer.parseInt(sc.next());
      B[i] = Long.parseLong(sc.next());
    }
    TreeSet<Range> ranges = new TreeSet<>();
    ranges.add(new Range(0, 0));
    ranges.add(new Range(N, -1));
    for (int i = 0; i < Q; i++) {
      Range cur = ranges.lower(new Range(A[i], 0));
      Range next = ranges.higher(cur);
      if (A[i] != next.start) {
        next = new Range(A[i], cur.count);
        ranges.add(next);
      }
      while (true) {
        Range prev = ranges.lower(cur);
        int len = next.start - cur.start;
        if (prev == null || (prev.count - cur.count - 1) * len >= B[i]) {
          cur.count += B[i] / len;
          if (B[i] % len != 0) {
            ranges.add(new Range(cur.start + (int)(B[i] % len), cur.count));
            cur.count++;
          }
          break;
        } else if ((prev.count - cur.count) * len >= B[i]) {
          if (B[i] % len != 0) {
            cur.start += B[i] % len;
            cur.count += B[i] / len;
          } else {
            ranges.remove(cur);
          }
          break;
        } else {
          B[i] -= (prev.count - cur.count) * len;
          ranges.remove(cur);
          cur = prev;
        }
      }
    }
    StringBuilder sb = new StringBuilder();
    ArrayList<Range> rangeList = new ArrayList<>(ranges);
    for (int i = 0; i < rangeList.size() - 1; i++) {
      for (int j = 0; j < rangeList.get(i + 1).start - rangeList.get(i).start; j++) {
        sb.append(rangeList.get(i).count + "\n");
      }
    }
    System.out.print(sb);
  }

  static class Range implements Comparable<Range> {
    int start;
    long count;

    public Range(int start, long count) {
      this.start = start;
      this.count = count;
    }

    @Override
    public int compareTo(Range o) {
      return Integer.compare(this.start, o.start);
    }

    @Override
    public boolean equals(Object o) {
      if (this == o) return true;
      if (o == null || getClass() != o.getClass()) return false;
      Range range = (Range) o;
      return start == range.start;
    }

    @Override
    public int hashCode() {
      return start;
    }

    @Override
    public String toString() {
      return "Range{" +
          "start=" + start +
          ", count=" + count +
          '}';
    }
  }
}
