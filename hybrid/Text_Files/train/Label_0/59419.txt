import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.util.*;
import java.io.IOException;
import java.lang.*;

public class JavaApplication7 {
    static int[] winners;
    static int ans;
    
    public static boolean contains(final int[] array, final int key) {
    for (final int i : array) {
        if (i == key) {
            return true;
        }
    }
    return false;
}
    
    public static void findwinners(int s)
    {
    int i = (s/50) % 475;
    for (int j = 0; j<25;j++)
    {
        i =(i * 96 + 42) % 475;
        winners[j]=26 + i; 
    }  
    }

    public static void main(String[] args) throws IOException{
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    PrintWriter pw = new PrintWriter(System.out);
    StringTokenizer st = new StringTokenizer(br.readLine());
    int p = Integer.parseInt(st.nextToken());
    int x = Integer.parseInt(st.nextToken());
    int y = Integer.parseInt(st.nextToken());
    winners = new int[25];
    int z = x;
    while(z>=y+50)
    {
        z=z-50;
    }   
    //int target;
    findwinners(z);
    while(!contains(winners,p))
    {
        z=z+50;
        findwinners(z);   
        
         
    }
    //pw.println(z);
    //for(int i=0;i<25;i++){
    //pw.println(winners[i]);}
    if(x>=z) ans=0;
    else ans = (z+50-x)/100;
    pw.println(ans);
    pw.close();
    }
    
}