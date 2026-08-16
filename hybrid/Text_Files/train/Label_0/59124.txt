import java.io.*;
import java.util.*;

public class CF396E {
	public static void main(String[] args) throws Exception {
		BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter writer = new BufferedWriter(new OutputStreamWriter(System.out));
		TaskSolver solver = new TaskSolver(reader, writer);
		solver.solve();
		reader.close();
		writer.close();
	}
	
	/*private static Random randGen = new Random();
	
	private static String randomTest() {
		StringBuilder str = new StringBuilder();
		int n = randGen.nextInt(20) + 1, k = randGen.nextInt(10) + 1;
		str.append(n).append(" ").append(k).append("\n");
		for (int i = 0; i < n; i++) {
			int x = randGen.nextInt(10) + 1;
			int r = randGen.nextInt(10) + 1;
			int f = randGen.nextInt(20) + 1;
			str.append(x).append(" ").append(r).append(" ").append(f).append("\n");
		}
		return str.toString();
	}
	
	public static void main(String[] args) throws Exception {
		BufferedWriter writer = new BufferedWriter(new OutputStreamWriter(System.out));
		for (;;) {
			String test = randomTest();
			BufferedReader reader = new BufferedReader(new StringReader(test));
			System.out.print(test);
			TaskSolver solver = new TaskSolver(reader, writer);
			solver.solve();
			reader.close();
			writer.flush();
		}
	}*/
}

class RadioStation {
	public int x;
	public int r;
	public int f;
	
	public RadioStation(int aX, int aR, int aF) {
		x = aX;
		r = aR;
		f = aF;
	}
	
	public RadioStation(String s) {
		StringTokenizer tokenizer = new StringTokenizer(s);
		x = Integer.parseInt(tokenizer.nextToken());
		r = Integer.parseInt(tokenizer.nextToken());
		f = Integer.parseInt(tokenizer.nextToken());
	}
	
	public final String toString() {
		StringBuilder builder = new StringBuilder();
		builder.append(x).append(" ").append(r).append(" ").append(f);
		return builder.toString();
	}
}

class Event implements Comparable<Event> {
	public static enum EventType {
		OPEN, 
		CLOSE;
		
		public int toInteger() {
			return (this == OPEN) ? 0 : 1;
		}
	}
	
	public int t;
	public EventType type;
	public RadioStation station;
	
	public Event(EventType aType, RadioStation aStation) {
		type = aType;
		station = aStation;
		if (aType == EventType.OPEN) {
			t = aStation.x;
		} else {
			t = aStation.x + aStation.r;
		}
	}
	
	@Override
	public int compareTo(Event o) {
		if (this.t < o.t) {
			return -1;
		}
		if (this.t > o.t) {
			return 1;
		}
		if (this.type.toInteger() < o.type.toInteger()) {
			return -1;
		}
		if (this.type.toInteger() > o.type.toInteger()) {
			return 1;
		}
		return 0;
	}
}

class FenwickTree {
	private int n;
	private int v[];
	
	public final void modify(int i, int delta) {
		while (i < n) {
			v[i] += delta;
			i |= i + 1;
		}
	}
	
	public final int sum(int i) {
		int res = 0;
		while (i >= 0) {
			res += v[i];
			i &= i + 1;
			i--;
		}
		return res;
	}
	
	public final int sum(int l, int r) {
		if (l > r) {
			return 0;
		} else {
			return sum(r) - sum(l-1);
		}
	}
	
	public FenwickTree(int pN) {
		n = pN;
		v = new int[n];
	}
}

class TaskSolver {
	private static class IntegerList extends Vector<Integer> {
		public final int lowerBound(int key) {
			// first one >= key
			if (isEmpty()) {
				return 0;
			}
			if (lastElement() < key) {
				return size();
			}
			int l = 0, r = size() - 1;
			while (l < r) {
				int m = (l + r) / 2;
				if (elementAt(m) >= key) {
					r = m;
				} else {
					l = m+1;
				}
			}
			return l;
		}
		
		public final int upperBound(int key) {
			// last one <= key
			if (isEmpty()) {
				return -1;
			}
			if (firstElement() > key) {
				return -1;
			}
			int l = 0, r = size() - 1;
			while (l < r) {
				int m = (l + r + 1) / 2;
				if (elementAt(m) <= key) {
					l = m;
				} else {
					r = m-1;
				}
			}
			return l;
		}
	}
	
	private BufferedReader reader;
	private BufferedWriter writer;	
	private FenwickTree[] fenwicks;
	private IntegerList[] coords;
	private int n, k;
	private RadioStation[] stations;
	
	public TaskSolver(BufferedReader aReader, BufferedWriter aWriter) {
		reader = aReader;
		writer = aWriter;	
		fenwicks = new FenwickTree[10001];
		coords = new IntegerList[10001];
	}
	
	private final void add(int x, int f, int delta) throws Exception {
		int i = Collections.binarySearch(coords[f], x);
		fenwicks[f].modify(i, delta);
	}
	
	private final long count(int l, int r, int f) throws Exception {
		if (f < 0 || f >= coords.length) {
			return 0;
		}
		/*StringBuilder builder = new StringBuilder();
		builder.append("----------------\n");
		builder.append("Old: ").append(l).append(' ').append(r).append('\n');
		builder.append(coords[f]).append('\n');*/
		
		l = coords[f].lowerBound(l);
		r = coords[f].upperBound(r);
		
		/*builder.append("New: ").append(l).append(' ').append(r).append('\n');
		writer.write(builder.toString());
		builder.append("----------------\n");*/
		
		return fenwicks[f].sum(l, r);
	}
	
	private static IntegerList sortAndCompress(IntegerList v) {
		if (v.isEmpty()) {
			return v;
		}
		Collections.sort(v);
		IntegerList q = (IntegerList)v.clone();
		v.clear();
		v.add(q.elementAt(0));
		for (int i = 1; i < q.size(); i++) {
			if (q.elementAt(i) != q.elementAt(i-1)) {
				v.add(q.elementAt(i));
			}
		}
		return v;
	}
	
	public void solve() throws Exception {
		StringTokenizer token = new StringTokenizer(reader.readLine());
		n = Integer.parseInt(token.nextToken());
		k = Integer.parseInt(token.nextToken());
		stations = new RadioStation[n];
		Vector<Event> events = new Vector<Event>();
		for (int i = 0; i < coords.length; i++) {
			coords[i] = new IntegerList();
		}
		for (int i = 0; i < n; i++) {
			stations[i] = new RadioStation(reader.readLine());
			coords[stations[i].f].add(stations[i].x);
			events.add(new Event(Event.EventType.OPEN, stations[i]));
			events.add(new Event(Event.EventType.CLOSE, stations[i]));
		}	
		Collections.sort(events);
		long res = 0;
		/*long naiveRes = 0;
		for (int i = 0; i < n; i++) {
			for (int j = 0; j < i; j++) {
				if (Math.min(stations[i].r, stations[j].r) >= 
				    Math.abs(stations[i].x - stations[j].x)) {
					if (Math.abs(stations[i].f - stations[j].f) <= k) {
						naiveRes++;
					}
				}
			}
		}*/
		for (int i = 0; i < coords.length; i++) {
			coords[i] = sortAndCompress(coords[i]);
			fenwicks[i] = new FenwickTree(coords[i].size());
		}
		for (int i = 0; i < events.size(); i++) {
			Event curEvent = events.elementAt(i);
			RadioStation cur = curEvent.station;
			if (curEvent.type == Event.EventType.OPEN) {
				for (int j = cur.f - k; j <= cur.f + k; j++) {
					res += count(cur.x - cur.r, cur.x, j);
				}
				add(cur.x, cur.f, +1);
			} else {
				add(cur.x, cur.f, -1);
			}
		}
		/*if (res != naiveRes) {
			StringBuilder builder = new StringBuilder();
			builder.append("Answers aren\'t equal: expected ")
			       .append(naiveRes).append(", found ")
			       .append(res);
			writer.write(builder.toString());
			writer.newLine();
			writer.flush();
			for (;;);
		} else {
			StringBuilder builder = new StringBuilder();
			builder.append("Answer is correct: ").append(res);
			writer.write(builder.toString());
			writer.newLine();
		}*/
		writer.write(Long.toString(res));
	}
}
