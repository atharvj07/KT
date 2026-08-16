import java.io.*;
import java.util.*;

public class Main { //m-solutions2019 A -  
	
	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		int n = Integer.parseInt(st.nextToken());
		System.out.println((n-2)*180);
	}

}
