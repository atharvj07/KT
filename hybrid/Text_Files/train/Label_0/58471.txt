import java.util.*;
import java.io.*;

public class A {
	public static void main(String[] args) {

		Scanner sc = new Scanner(System.in);

		int N = sc.nextInt();
		int s = sc.nextInt();

		Person[] p = new Person[N];

		for(int i = 0; i < N; ++i) {
			p[i] = new Person(sc.nextInt(), sc.nextInt());
		}

		Arrays.sort(p);

		//for(Person pp: p)
		//	System.out.println(pp.floor + " " + pp.time);
	
		int currF = s;
		int currT = 0;

		for(int i = 0; i < N; ++i) {
			currT += currF - p[i].floor;
			currF = p[i].floor;
			if(currT < p[i].time)
				currT = p[i].time;
		}

		System.out.println(currT + currF);
	}
}

class Person implements Comparable<Person> {
	int floor;
	int time;

	public Person(int f, int t) {
		floor = f;
		time = t;
	}

	public int compareTo(Person p) {
		return p.floor - floor;
	}
}