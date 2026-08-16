import java.util.*;
import java.io.*;
public class codeforces {
    public static void main(String[] args) throws Exception {
        Scanner in=new Scanner(System.in);
        String s=in.next();
        boolean found=false;
        int i=0,count=0;
        while(i<s.length()){
            if(s.charAt(i)=='1'){
                found=true;
                break;
            }
         i++;
        }
        int j=i+1;
        while(found==true && j<s.length()){
              if(s.charAt(j)=='0'){
                  count++;
              }
            j++;
        }
        if(count>=6){
            System.out.println("YES");
        }
        else{
            System.out.println("NO");
        }
        in.close();
        return;
    }
}

