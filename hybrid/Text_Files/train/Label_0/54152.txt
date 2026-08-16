import java.util.*;
import java.lang.*;
import java.math.*;

public class Main {
	Scanner sc = new Scanner(System.in);
	void run(){
		for(;sc.hasNext();){
			String buffer= sc.next();
			
			String buffer2 = new String(buffer);
			int ans = 0;
			for(;buffer.indexOf("JOI") != -1;ans++){
				buffer = buffer.substring(buffer.indexOf("JOI")+1);
			}
			
			int ans2 = 0;
			for(;buffer2.indexOf("IOI") != -1;ans2++){
				buffer2 = buffer2.substring(buffer2.indexOf("IOI")+1);
			}
			System.out.println(ans);
			System.out.println(ans2);
			
		}
		
	}
	public static void main(String[] args){
		Main m = new Main();
		m.run();
	}
}