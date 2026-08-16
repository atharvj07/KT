import java.awt.geom.*;
import java.io.*;
import java.util.*;


public class Main {
	String cap = "12121414";
	
	private void doit(){
		Scanner sc = new Scanner(System.in);
		while(sc.hasNext()){
			int [] data = new int[8];
			for(int i = 0; i < 8; i++){
				data[i] = sc.nextInt();
			}
			
			int min = 1 << 24;
			StringBuilder ans = new StringBuilder();
			for(int i = 0; i < 8;i++){
				int count = 0;
				for(int j = 0; j < 8; j++){
					int v = data[j] - Math.min(data[j], cap.charAt((i+j) % 8) - '0');
					count += v;
				}
				if(count < min){
					min = count;
					ans = new StringBuilder();
					for(int j = 0; j < 8;j++){
						ans.append(cap.charAt((i+j) % 8));
					}
				}
				else if(count == min){
					StringBuilder sb = new StringBuilder();
					for(int j = 0; j < 8; j++){
						sb.append(cap.charAt((i+j) % 8));
					}
					if(ans.toString().compareTo(sb.toString()) > 0){
						ans = sb;
					}
				}
			}
			for(int i = 0; i < 7; i++){
				System.out.print(ans.charAt(i) + " ");
			}
			System.out.println(ans.charAt(7));
		}
	}

	public static void main(String [] args){
		new Main().doit();
	}
}