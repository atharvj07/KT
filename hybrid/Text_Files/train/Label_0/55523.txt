import java.util.*;

public class Main{
        public static void main(String[] args){

        int n;
        int x,y,dx,dy;
        int xmax,ymax;
        int d,dmax;

        Scanner kbd=new Scanner(System.in);

        n=kbd.nextInt();
        x=0;
        y=0;
        d=0;

        for(int i=0; i<n; i++){
        dmax=0;
        xmax=0;
        ymax=0;
        while(true){
           dx=kbd.nextInt();
           dy=kbd.nextInt();
           x+=dx;
           y+=dy;
           d=x*x+y*y;
           if(dmax<d){
              dmax=d;
              xmax=x;
              ymax=y;
           } else if(dmax==d){
                if(x>xmax){
                xmax=x;
                ymax=y;
                }
           }
           if(dx==0 && dy==0){
                System.out.println(xmax+" "+ymax);
                break;
                }
           }
        }

        }
}