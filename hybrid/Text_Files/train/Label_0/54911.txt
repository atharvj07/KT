import java.util.*;

class Main{
    private void compute(){
        int i, j, k, r, c;
        int cnt = 0;
        int ans = 0;
        int tmp = 0;
        String inStr, tmpStr;
        char tmpChar;

        Scanner sc = new Scanner(System.in);
        int C = sc.nextInt();
        int N = sc.nextInt();
        int[][] p = new int[N+1][N+1];

        for (i = 1; i <= N; i++){
            inStr = sc.next();
            for (j = 1; j <= N; j++){
                tmpChar = inStr.charAt(j - 1);
                p[i][j] = Character.getNumericValue(tmpChar);
            }
        }


        cnt = 1;
        out_of_loop:
        for (i = 1; i <= (N / 2); i++){
            for (j = 1; j <= (N / 2); j++){
                if ((p[i][j] != p[i][N+1-j]) || (p[i][j] != p[N+1-i][j]) || (p[i][j] != p[N+1-i][N+1-j])){
                    cnt--;
                    break out_of_loop;
                }
            }
        }

        for (i = 2; i <= C; i++){
            int D = sc.nextInt();
            for (j = 1; j <= D; j++){
                r = sc.nextInt();
                c = sc.nextInt();
                switch (p[r][c]){
                case 0:
                    p[r][c] = 1;
                    break;
                case 1:
                    p[r][c] = 0;
                    break;
                }
            }

            cnt++;
            out_of_loop:
            for (j = 1; j <= (N / 2); j++){
                for (k = 1; k <= (N / 2); k++){
                    if ((p[j][k] != p[j][N+1-k]) || (p[j][k] != p[N+1-j][k]) || (p[j][k] != p[N+1-j][N+1-k])){
                        cnt--;
                        break out_of_loop;
                    }
                }
            }
        }

        System.out.println(cnt);
    }
    public static void main(String[] arg){
        new Main().compute();
    }
}
