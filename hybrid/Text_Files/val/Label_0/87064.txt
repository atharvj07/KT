import java.io.*;
public final class Main{
    public static void main(String args[]) throws Exception{
        BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
        int a[][]=new int[5][5];
        int g=0,h=0;
        for(int i=0;i<5;i++){
            String str=br.readLine();
            String s[]=str.split(" ");
            for(int j=0;j<5;j++){
                int x=Integer.parseInt(s[j]);
                a[i][j]=x;
                if(x==1){
                    g=i+1;
                    h=j+1;
                }
            }
        }
        int l=Math.abs(g-3);
        l+=Math.abs(h-3);
        System.out.println(l);
    }
}