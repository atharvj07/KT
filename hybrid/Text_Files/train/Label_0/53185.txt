import java.io.*;
import java.util.*;
public class CF_476D {
    public static void main(String[] args) throws IOException {
        new CF_476D().solve();
    }
    
    
    void solve() throws IOException{
        
        InputStream in = System.in;
        PrintStream out = System.out;
        
//        in = new FileInputStream("in.txt");
//        out = new PrintStream("out.txt");
        
        Scanner sc=new Scanner(in);
        int n=sc.nextInt(), k=sc.nextInt();
        
        int max=0;
        StringBuilder ans=new StringBuilder();
        for (int i=0;i<n;i++){
            ans.append(k*(6*i+1)+" "+k*(6*i+2)+" "+k*(6*i+3)+" "+k*(6*i+5)+"\n");
            max=k*(6*i+5);
        }
        out.println(max);
        out.println(ans.toString());
            
        
    }
}


