


import java.util.*;


public class Main {
    
    public static void main(String[] args){
        Scanner input = new Scanner(System.in);
        
       int n;
       n = input.nextInt();
       int a[][] = new int[n][2];
        for (int i = 0; i < n; i++) {
            a[i][0] = input.nextInt();
            a[i][1] = input.nextInt();
        }
        
        Arrays.sort(a,(x,y)->(x[0]-y[0]));
        Arrays.sort(a,(x,y)->(x[1]-y[1]));
        long points=a[n-1][0];
        int iCanPlay=a[n-1][1];
        
        
        for (int i = n-2; i >=0; i--) {
            
            if(iCanPlay>0)
            {
                
                points+=a[i][0];
                iCanPlay--;
                iCanPlay+=a[i][1];
            }
            else
                break;
        }
        System.out.println(points);
        
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               
    }
}

