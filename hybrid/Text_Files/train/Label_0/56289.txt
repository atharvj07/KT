import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main{
	public static void main(String[] args)throws IOException{
		InputStreamReader isr = new InputStreamReader(System.in);
		BufferedReader reader = new BufferedReader(isr);
		String string, mf = "";
		int max, hoge;
		
		while(!(string = reader.readLine()).equals("0 0")){
			max = 0;
			for(int i = 0; i < 4; i++){
				hoge = Integer.valueOf(string.split(" ")[0]) +
					   Integer.valueOf(string.split(" ")[1]);
				max = Math.max(max, hoge);
				
				if(max == hoge){
					mf = String.valueOf((char)(65 + i));
				}
				string = reader.readLine();
			}
			max = Math.max(max, hoge = Integer.valueOf(string.split(" ")[0]) +
					   			Integer.valueOf(string.split(" ")[1]));
			if(max == hoge){
				mf = String.valueOf((char)(65 + 4));
			}
			
			System.out.println(mf + " " + max);
		}
	}
}