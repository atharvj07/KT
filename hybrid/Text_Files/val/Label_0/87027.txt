import java.awt.geom.*;
import java.util.*;
 
public class Main {
    Scanner sc = new Scanner(System.in);
 
    public static void main(String[] args) {
        new Main(); 
    }
 
    public Main() {
    	new aoj0058().doIt();
    }
    class aoj0058{
    	void doIt(){
    		while(sc.hasNext()){
                double x1=sc.nextDouble();
                double y1=sc.nextDouble();
                double x2=sc.nextDouble();
                double y2=sc.nextDouble();
                double x3=sc.nextDouble();
                double y3=sc.nextDouble();
                double x4=sc.nextDouble();
                double y4=sc.nextDouble();  
                if(Math.abs((x2-x1)*(x4-x3)+(y2-y1)*(y4-y3))<1e-10)System.out.println("YES");
                else System.out.println("NO");
            }
    	}
    }
}