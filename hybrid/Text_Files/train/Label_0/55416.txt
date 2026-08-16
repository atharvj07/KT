import java.util.Scanner;
import java.util.ArrayList;
import java.util.List;
import java.util.Collections;

public class carrepairshop {
	public static void main(String[] args) {
		Scanner in = new Scanner(System.in);
		int n = in.nextInt();
		List<range> list = new ArrayList<range>();
		List<range> orig = new ArrayList<range>();
		for (int i=0; i<n; i++) {
			long s = in.nextLong();
			long e = in.nextLong()+s-1;
			boolean valid = true;
			for (int j=0; j<list.size(); j++) {
				range r = list.get(j);
				if(s>r.max || (s<r.min && e<r.min)) {
					continue;
				} else {
					valid = false;
					break;
				}
			}
			if(!valid) {
				long dist = e-s;
				long start = 1;
				for (int j=0; j<list.size(); j++) {
					range r = list.get(j);
					if(r.min>(dist+start)) {
						break;
					} else {
						start = r.max+1;
					}
				}
				list.add(new range(start, start+dist));
				orig.add(new range(start, start+dist));
			} else {
				list.add(new range(s,e));
				orig.add(new range(s,e));
			}
			Collections.sort(list);
		}
		for (range r : orig) {
			System.out.println(r.min+" "+r.max);
		}

	}
}

class range implements Comparable<range>{
	long min;
	long max;
	public range(long min, long max) {
		this.min = min;
		this.max = max;
	}

	public int compareTo(range other) {
		return (this.min-other.min<0)?-1:1;
	}
}