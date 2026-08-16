import java.util.*;
import java.io.*;

public class Main {

    static boolean checker(char[][] arr,int i,int j){
           int rightCount=0,leftCount=0,upCount=0,downCount=0,countUpLeft=0,countUpRight=0,countDownLeft=0,countDownRight=0;
           boolean itself=false,dotH=false,dotV=false,dotD1=false,dotD2=false;
           if(arr[i][j]=='X') itself=true;
           int k=j+1;
           while(k<10){
               if(arr[i][k]=='X') rightCount++;
               else if (arr[i][k]=='.') {dotH=true; break;}
               else break;
               k++;
           }
           k=j-1;
           while(k>=0){
               if(arr[i][k]=='X') leftCount++;
               else if (arr[i][k]=='.'){dotH=true; break;}
               else break;
               k--;
           }
           k=i-1;
           while(k>=0){
               if(arr[k][j]=='X') upCount++;
               else if (arr[k][j]=='.'){dotV=true; break;}
               else break;
               k--;
           }
           k=i+1;
           while(k<10){
            if(arr[k][j]=='X') downCount++;
            else if (arr[k][j]=='.'){dotV=true; break;}
            else break;
            k++;
           }
           int k1=i-1;
           int k2=j-1;
           while(k1>=0 && k2>=0){
               if(arr[k1][k2]=='X') countUpLeft++;
               else if (arr[k1][k2]=='.'){dotD1=true; break;}
               else break;
               k1--;
               k2--;
           }
           k1=i+1;
           k2=j+1;
           while(k1<10 && k2<10){
            if(arr[k1][k2]=='X') countDownRight++;
            else if (arr[k1][k2]=='.'){dotD1=true; break;}
            else break;
            k1++;
            k2++;
           }
           k1=i-1;
           k2=j+1;
           while(k1>=0 && k2<10){
            if(arr[k1][k2]=='X') countUpRight++;
            else if (arr[k1][k2]=='.'){dotD2=true; break;}
            else break;
            k1--;
            k2++;
           }
           k1=i+1;
           k2=j-1;
           while(k1<10 && k2>=0){
            if(arr[k1][k2]=='X') countDownLeft++;
            else if (arr[k1][k2]=='.'){dotD2=true; break;}
            else break;
            k1++;
            k2--;
           }

           if(itself){
               if ( leftCount+rightCount>=4 || upCount+downCount>=4 || countUpLeft+countDownRight>=4 || countUpRight+countDownLeft>=4) return true;
               else if (leftCount+rightCount==3 && dotH) return true;
               else if (countUpLeft+countDownRight==3 && dotD1) return true;
               else if (countUpRight+countDownLeft==3 && dotD2) return true;
               else return upCount + downCount == 3 && dotV;
           }else{
               return leftCount + rightCount >= 4 || upCount + downCount >= 4 || countUpLeft+countDownRight>=4 || countUpRight+countDownLeft>=4;
           }

    }
    public static void main(String[] args) throws IOException {
        //Code starts
        FastReader ip = new FastReader();
        OutputStream output = System.out;
        PrintWriter out = new PrintWriter(output);
        char[][] arr=new char[10][10];
        for(int i=0;i<10;i++){
            String s=ip.nextLine();
            for(int j=0;j<10;j++){
                arr[i][j]=s.charAt(j);
            }
        }
        boolean ans=false;
        for(int i=0;i<10;i++){
            for(int j=0;j<10;j++){
                if(arr[i][j]!='O' && checker(arr,i,j)){
                    ans=true;
                    break;
                }
            }
            if(ans) break;
        }

        if(ans){
            out.println("YES");
        }else{
            out.println("NO");
        }
        out.close();
        //Code ends
    }

    static class FastReader {
        BufferedReader br;
        StringTokenizer st;
        FastReader() { br = new BufferedReader(new InputStreamReader(System.in)); }
        String next() { while (st == null || !st.hasMoreElements()) {
            try { st = new StringTokenizer(br.readLine()); }
            catch (IOException e) { e.printStackTrace(); } }
            return st.nextToken();
        }

        int nextInt() { return Integer.parseInt(next()); }
        long nextLong() { return Long.parseLong(next()); }
        double nextDouble() { return Double.parseDouble(next()); }

        String nextLine() {
            String str = "";
            try { str = br.readLine(); }
            catch (IOException e) { e.printStackTrace(); }
            return str;
        }
    }

}