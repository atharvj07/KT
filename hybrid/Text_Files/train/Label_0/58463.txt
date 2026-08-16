import java.io.*;

public class Main {
	public static void main(String[] args) {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		try {
			String line;
			while(true){
				/* input */
				line = br.readLine();

				int n = Integer.parseInt(line);

				if(n==0) break;

				String[] str = br.readLine().split(" ");
				
				/* processing */
				int sum = 0;
				for(int i=0;i<str.length;i++){
					sum += Integer.parseInt(str[i]);
				}
				
				/* output */
				System.out.println(sum/(n-1));
			}
		} catch (IOException e) {
			e.printStackTrace();
		}
	}
}