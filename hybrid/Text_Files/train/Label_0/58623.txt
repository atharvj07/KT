import java.util.*;
public class Main {

    public static void main(String[] args)
    {
        Scanner ab=new Scanner (System.in);
        int x=ab.nextInt();
        double k[]=new double[x];
        double sum=0;
        for(int g=0;g<x;g++)
        {
            k[g]=ab.nextDouble();
            sum+=k[g];
        }
        
        
        
        double sum1=0;
        for(int y=0;y<x;y++)
        {
            sum1+=k[y];
            if(sum1>=sum/2.0)
            {
                System.out.println(y+1);
                            break;

            }
        }
    }
    
}
