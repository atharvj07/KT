import java.util.*;

public class Main {
	
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		while(sc.hasNext()){
            String[] s =  sc.next().split(",");
            double[] x = new double[6];
            double[] y = new double[6];
			for(int i=0;i<6;i++){
				if(i<4){
					x[i] = Double.valueOf(s[2*i]);
					y[i] = Double.valueOf(s[2*i+1]);
				}else{
					x[i] = x[i-4];
					y[i] = y[i-4];
				}
			}
			
			boolean flag = true;
            double x1, y1, x2, y2;
            double res = 0;
            for(int i=0;i<4;i++){
            	x1 = x[i+1]-x[i];
            	y1 = y[i+1]-y[i];
            	x2 = x[i+2]-x[i];
            	y2 = y[i+2]-y[i];
            	if(i==0){
            		res = x1*y2-x2*y1;
            	}else if(res*(x1*y2-x2*y1)<0){
            		flag = false;
            		break;
            	}
            }
			
            if(flag==true) System.out.println("YES");
            else System.out.println("NO");
		}
	}	
}