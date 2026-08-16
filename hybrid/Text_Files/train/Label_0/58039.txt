import java.io.*;
import java.util.StringTokenizer;

public class Program_2 {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        int t = Integer.parseInt(br.readLine());
        int n;
        int[] arr;
        int[] c;
        int targetNum;
        int count;
        StringTokenizer st;
        for (int i = 0; i < t; i++) {
            n = Integer.parseInt(br.readLine());
            arr = new int[n];
            targetNum = n/3;
            c = new int[3];
            count = 0;
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < n; j++)
                arr[j] = Integer.parseInt(st.nextToken());
            int temp;
            for (int j = 0; j < n; j++) {
                temp = arr[j]%3;
                c[temp]++;
            }

            while(true) {
                if (targetNum < c[0]) {
                    c[0]--;
                    c[1]++;
                    count++;
                }

                if (targetNum < c[1]) {
                    c[1]--;
                    c[2]++;
                    count++;
                }

                if (targetNum < c[2]) {
                    c[2]--;
                    c[0]++;
                    count++;
                }

                if (c[0] == targetNum && c[1] == targetNum && c[2] == targetNum)
                    break;
            }
            bw.write(count+"\n");
        }
        bw.flush();
    }
}