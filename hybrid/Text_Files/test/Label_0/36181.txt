import java.util.*;
import java.lang.*;
import java.io.*;


public class Foobar {
	static class FastReader {
		BufferedReader br;
		StringTokenizer st;
 
		public FastReader() {
			br = new BufferedReader(new InputStreamReader(System.in));
		}
 
		String next() {
			while (st == null || !st.hasMoreElements()) {
				try {
					st = new StringTokenizer(br.readLine());
				} catch (IOException e) {
					e.printStackTrace();
				}
			}
			return st.nextToken();
		}
 
		int nextInt() {
			return Integer.parseInt(next());
		}
 
		long nextLong() {
			return Long.parseLong(next());
		}
 
		double nextDouble() {
			return Double.parseDouble(next());
		}
 
		String nextLine() {
			String str = "";
			try {
				str = br.readLine();
			} catch (IOException e) {
				e.printStackTrace();
			}
			return str;
		}
	} 
static void Input(){

   try {
    FileOutputStream output=new FileOutputStream("output.txt");
    PrintStream out=new PrintStream(output);
    //Diverting the output stream into file "temp.out".Comment the below line to use console
    System.setOut(out);
    
    InputStream input=new FileInputStream("input.txt");
    //Diverting the input stream into file "temp.in".Comment the below line to use console
    System.setIn(input);
    
   } catch (FileNotFoundException e) {
    e.printStackTrace();
   }
}
 static class skill{
 	int height;
 	int index;
 	int tower;
 	skill(int height,int index){
 		this.height=height;
 		this.index=index;
 		this.tower=-1;
 	}
 } 
  static class skill2{
 	int sum;
 	int tower;

 	skill2(int sum,int tower){
 		this.sum=sum;
 		this.tower=tower;
 	}
 } 
 static class sort implements Comparator<skill>{
	@Override
	public int compare(skill node0,skill node1){
		return node0.height-node1.height;
	}
}
 static class sort2 implements Comparator<skill>{
	@Override
	public int compare(skill node0,skill node1){
		return node0.index-node1.index;
	}
}
 static class sort3 implements Comparator<skill2>{
	@Override
	public int compare(skill2 node0,skill2 node1){
		return node0.sum-node1.sum;	
	}
}

public static void main(String args[]) throws Exception
{
//Input();
FastReader sc=new FastReader();
int t=sc.nextInt();
for (int test=1;test<=t;test++){
	int n=sc.nextInt();
	String str=sc.nextLine();
	int flag=0;
	for(int i=0;i<n-1;i++){
		if(str.charAt(i)!=str.charAt(i+1)){
			for(int j=i+1;j<n;j++){
				if(str.charAt(i)==str.charAt(j)){
					flag=1;
					break;
				}
			}
		}
	}
	if(flag==1){
		System.out.println("NO");
	}
	else{
System.out.println("YES");
	}

}
}
}

// 	XOR OR
// 11	0	1
// 10	1	1
// 01	1	1
// 00	1	0