import java.io.BufferedOutputStream;
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.util.StringTokenizer;

public class altseq {

	public static void main(String[] args) throws Exception {
		BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
		PrintWriter out = new PrintWriter(new BufferedOutputStream(System.out));

		int t = Integer.parseInt(in.readLine());
		
		for (int i = 0; i < t; i++) {
			int n = Integer.parseInt(in.readLine());
			
			StringTokenizer st = new StringTokenizer(in.readLine());
			int[] nums = new int[n];
			for (int j = 0; j < n; j++) {
				nums[j] = Integer.parseInt(st.nextToken());
			}
			
			int curr = nums[0];
			long sum = 0;
			
			for (int j = 1; j < n; j++) {
				if((nums[j] > 0 && nums[j-1] > 0) || (nums[j] < 0 && nums[j-1] < 0)) {
					curr = Math.max(curr, nums[j]);
				} else {
					sum += curr;
					curr = nums[j];
				}
			}
			
			sum += curr;
			
			out.println(sum);
		}
		
		in.close();
		out.close();
	}
	
}
