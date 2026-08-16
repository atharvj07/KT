import java.io.*;
import java.util.*;

public class Main {
  public static void main(String[] args) throws IOException {
    BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));

    StringTokenizer tokenizer = new StringTokenizer(reader.readLine());
    int w = Integer.parseInt(tokenizer.nextToken());
    int h = Integer.parseInt(tokenizer.nextToken());
    int n = Integer.parseInt(tokenizer.nextToken());

    TreeSet<CountHolder> widths = new TreeSet<CountHolder>();
    TreeSet<CountHolder> heights = new TreeSet<CountHolder>();

    TreeSet<Section> xSections = new TreeSet<Section>();
    TreeSet<Section> ySections = new TreeSet<Section>();

    widths.add(new CountHolder(w, 1));
    xSections.add(new Section(0, w));

    heights.add(new CountHolder(h, 1));
    ySections.add(new Section(0, h));

    for(int i = 0;i < n;i++) {
      tokenizer = new StringTokenizer(reader.readLine());

      char c = tokenizer.nextToken().charAt(0);
      int idx = Integer.parseInt(tokenizer.nextToken());

      if(c == 'H') {
        process(heights, ySections, idx);
      }
      else {
        process(widths, xSections, idx);
      }

      long cur = widths.last().value;
      cur *= heights.last().value;
      System.out.println(cur);
    }
  }

  private static void process(TreeSet<CountHolder> lengths, TreeSet<Section> sections, int idx) {
    Section dummy = new Section(idx, 0);
    Section actual = sections.floor(dummy);

    sections.remove(actual);
    sections.add(new Section(actual.start, idx-actual.start));
    sections.add(new Section(idx, actual.length-(idx-actual.start)));

    CountHolder holder = lengths.floor(new CountHolder(actual.length, 0));
    holder.count--;
    if(holder.count == 0) {
      lengths.remove(new CountHolder(actual.length, 0));
    }

    holder = lengths.floor(new CountHolder(idx-actual.start, 0));
    if(holder != null && holder.value == idx-actual.start) {
      holder.count++;
    }
    else {
      lengths.add(new CountHolder(idx-actual.start, 1));
    }

    holder = lengths.floor(new CountHolder(actual.length-(idx-actual.start), 0));
    if(holder != null && holder.value == actual.length-(idx-actual.start)) {
      holder.count++;
    }
    else {
      lengths.add(new CountHolder(actual.length-(idx-actual.start), 1));
    }
  }

  private static class Section implements Comparable<Section> {
    int start;
    int length;

    public Section(int start, int length) {
      this.start = start;
      this.length = length;
    }

    @Override
    public int compareTo(Section o) {
      return start-o.start;
    }
  }

  private static class CountHolder implements Comparable<CountHolder> {
    int value;
    int count;

    public CountHolder(int value, int count) {
      this.value = value;
      this.count = count;
    }

    @Override
    public int compareTo(CountHolder o) {
      return value-o.value;
    }
  }
}