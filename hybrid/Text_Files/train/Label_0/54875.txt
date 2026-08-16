    import java.util.Scanner;
     
    public class Main {
     
    static Scanner sc = new Scanner(System.in);
    static int H, W;
    static int[][] f;
     
    static void solve() {
    int[] rsum = new int[H];
    int[] csum = new int[W];
    int all = 0;
    for (int i = 0; i < H; ++i) {
    for (int j = 0; j < W; ++j) {
    if (f[i][j] == 0) {
    ++rsum[i];
    ++csum[j];
    }
    }
    all += rsum[i];
    }
    if (all != 0 && H * W % 2 != 0) {
    System.out.println("Impossible");
    return;
    }
    boolean[][] ans = new boolean[H][W];
    for (int i = 0; i < H; ++i) {
    for (int j = 0; j < W; ++j) {
    ans[i][j] = (rsum[i] + csum[j] - f[i][j]) % 2 != 0;
    }
    }
    StringBuilder sb = new StringBuilder();
    for (int i = 0; i < H; ++i) {
    for (int j = 0; j < W; ++j) {
    sb.append(ans[i][j] ? '0' : '1');
    if (j != W - 1) {
    sb.append(' ');
    }
    }
    sb.append('\n');
    }
    System.out.print(sb);
    }
     
    public static void main(String[] args) {
    H = sc.nextInt();
    W = sc.nextInt();
    f = new int[H][W];
    sc.nextLine();
    for (int i = 0; i < H; ++i) {
    String line = sc.nextLine();
    for (int j = 0; j < W; ++j) {
    f[i][j] = line.charAt(2 * j) - '0';
    }
    }
    solve();
    }
    }