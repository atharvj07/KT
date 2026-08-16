import java.util.Arrays;
import java.util.Comparator;
import java.util.Scanner;

public class Main {

    /**
     * @param args
     */
    public static void main(String[] args) {
        Scanner sc=new Scanner(System.in);
        while(true){
            int M = sc.nextInt();
            int T = sc.nextInt();
            int P = sc.nextInt();
            int R = sc.nextInt();
            if(M+T+P+R==0)break;
            int[][] pena = new int[T][P];
            int[][] score = new int[T][3];
            for (int i = 0; i < score.length; i++) {
                score[i][0]=i;
            }
            for (int i = 0; i < R; i++) {
                int m = sc.nextInt();
                int t = sc.nextInt()-1;
                int p = sc.nextInt()-1;
                int r = sc.nextInt();
                if(r==0){
                    score[t][1]++;
                    score[t][2]+=m+pena[t][p]*20;
                } else {
                    pena[t][p]++;
                }
            }
            Arrays.sort(score,new Comparator<int[]>(){
                @Override
                public int compare(int[] a, int[] b) {
                    if(a[1]==b[1]){
                        if(a[2]==b[2]){
                            return b[0]-a[0];
                        }
                        return a[2]-b[2];
                    }
                    return b[1]-a[1];
                }
            });
            StringBuilder ans=new StringBuilder();
            for (int i = 0; i < score.length; i++) {
                ans.append(score[i][0]+1);
                while(i+1<score.length && score[i][1]==score[i+1][1]&&score[i][2]==score[i+1][2]){
                    ans.append("=");
                    ans.append(score[i+1][0]+1);
                    i++;
                }
                ans.append(",");
            }
            System.out.println(ans.substring(0,ans.length()-1));
        }
    }

}