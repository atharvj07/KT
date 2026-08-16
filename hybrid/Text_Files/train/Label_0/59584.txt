import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.Stack;
import java.util.StringTokenizer;

public class Main {

	public class Activity implements Comparable<Activity> {
		int start;
		int end;
		public Activity(int start, int end) {
			this.start = start;
			this.end = end;
		}
		@Override
		public int compareTo(Activity o) {
			if (this.start != o.start) {
				return this.start - o.start;
			}
			return this.end - this.end;
		}
		
		public String toString() {
			return String.format("%d-%d", start, end);
		}
	}
	
	public static void main(String[] args) throws IOException {
		new Main().run();
	}
	
	private void run() throws IOException {
		BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
		int n = Integer.parseInt(reader.readLine());
		Activity[] activities = new Activity[n];
		for (int i = 0; i < n; i++) {
			StringTokenizer st = new StringTokenizer(reader.readLine());
			int start = Integer.parseInt(st.nextToken());
			int end = Integer.parseInt(st.nextToken());
			activities[i] = new Activity(start, end);
		}
		reader.close();
		
		Arrays.sort(activities);
		Stack<Activity> stack = new Stack<Activity>();
		stack.push(activities[0]);
		for (int i = 1; i < n; i++) {
			Activity last = stack.peek();
			Activity acti = activities[i];
			if (acti.start > last.end) {
				stack.push(acti);
			} else if (acti.end < last.end) {
				stack.pop();
				stack.push(acti);
			}
		}
		System.out.println(stack.size());
	}
}
