import java.util.*;
import java.io.*;

public class Main{
	public static void main(String[] args){
		Scanner stdIn = null;
		
		try{
			stdIn = new Scanner(new BufferedReader(new InputStreamReader(System.in)));
			while( stdIn.hasNext() ){
				String str = stdIn.next();
				String[] s = str.split(",");
				double[] p = new double[6];
				for(int i = 0; i < 6; i++){
					p[i] = Double.parseDouble(s[i]);
				}
				double px = p[2]-p[0];
				double py = p[3]-p[1];
				double ax = p[4]-p[0];
				double ay = p[5]-p[1];
				double t = (px*ax+py*ay)/(px*px+py*py);
				double ansx = 2*t*px-ax+p[0];
				double ansy = 2*t*py-ay+p[1];
				System.out.printf("%.6f %.6f%n", ansx, ansy);			
			}		
		} finally {
			if( stdIn != null){
				stdIn.close();
			}
		}
	}
}