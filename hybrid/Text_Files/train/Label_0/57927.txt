
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

public class D {
    static int MAX = (int) 2e5 + 1;

    public static void main(String[] args) throws IOException {
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        String[] S = in.readLine().split(" ");
        int n = Integer.parseInt(S[0]);
        int m = Integer.parseInt(S[1]);
        S = in.readLine().split(" ");
        int[] M = new int[n + 2];
        for (int i = 0; i < n; i++)
            M[i] = Integer.parseInt(S[i]);
        int[] C = new int[MAX];
        int[] stars = new int[m];
        S = in.readLine().split(" ");
        for (int i = 0; i < m; i++) {
            stars[i] = Integer.parseInt(S[i]);
            C[stars[i]]++;
        }
        M[n] = 0;
        M[n + 1] = MAX;
        for (int i = 1; i < MAX; i++)
            C[i] += C[i - 1];
        Arrays.sort(M);
        Arrays.sort(stars);
        int[] L = new int[n + 2];
        int[] R = new int[n + 2];
        L[1] = 1;
        for (int i = 2; i <= n; i++)
            if (M[i - 1] + 1 == M[i])
                L[i] = L[i - 1];
            else
                L[i] = i;
        R[n] = n;
        for (int i = n - 1; i > 0; i--)
            if (M[i] + 1 == M[i + 1])
                R[i] = R[i + 1];
            else
                R[i] = i;

        int[] D = new int[n + 2];
        int[] Z = new int[n + 2];
        for (int i = 1; i <= n; i++)
            if (L[i] == i) {
                D[i] = Z[L[i - 1]] + C[M[R[i]]] - C[M[i] - 1];
                for (int j = 0; j < m; j++) {
                    if (stars[j] < M[i]) {
                        if (i > M[i] - stars[j]) {
                            int monster = L[i - (M[i] - stars[j])];
                            D[i] = Math.max(D[i], Z[L[monster - 1]]
                                    + C[M[R[i]]] - C[M[i] - (i - monster) - 1]);
                        }
                    } else if (stars[j] > M[R[i]]) {
                        if (n - R[i] >= stars[j] - M[R[i]]) {
                            int monster = L[R[i] + stars[j] - M[R[i]]];
                            Z[monster] = Math.max(Z[monster], D[i]
                                    + C[M[R[i]] + (R[monster] - R[i])]
                                    - C[M[R[i]]]);
                        }
                    }
                }
                Z[i] = Math.max(Z[i], D[i]);
            }
        int max = 0;
        for (int i = 0; i <= n + 1; i++)
            max = Math.max(max, Z[i]);
        System.out.println(max);
    }
}