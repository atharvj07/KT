import java.util.*;

public class Main {
    private static final long MOD = 1000000007;
    
    public static void main(String[] args) throws Exception {
        Scanner scan = new Scanner(System.in);
        int taskCount = scan.nextInt();
        scan.nextLine();
        for (int taskIndex = 0; taskIndex < taskCount; taskIndex++) {
            if (taskIndex > 0) {
                scan.nextLine();
            }
            char[][] map = new char[8][];
            int x1 = -1, y1 = -1, x2 = -1, y2 = -1;
            for (int i = 0; i < 8; i++) {
                map[i] = scan.nextLine().toCharArray();
                for (int j = 0; j < 8; j++) {
                    if (map[i][j] == 'K') {
                        if (x1 == -1) {
                            x1 = i;
                            y1 = j;
                        } else {
                            x2 = i;
                            y2 = j;
                        }
                    }
                }
            }
            
            boolean pass = false;
            outer:
            for (int i = 0; i < 8; i++) {
                for (int j = 0; j < 8; j++) {
                    if (map[i][j] == '#') {
                        continue;
                    }
                    if ((x1 - i) % 2 != 0 || (x2 - i) % 2 != 0 || (y1 - j) % 2 != 0 || (y2 - j) % 2 != 0) {
                        continue;
                    } else if ((x1 - i + y1 - j) % 4 != 0 || (x2 - i + y2 - j) % 4 != 0) {
                        continue;
                    } else {
                        pass = true;
                        break outer;
                    }
                }
            }
            
            if (pass) {
                if ((x1 - x2) % 4 != 0) {
                    pass = false;
                }
            }
            System.out.println(pass ? "YES" : "NO");
        }
        
        scan.close();
    }
    
    private static void print(int... arr) {
        System.out.print(arr[0]);
        for (int i = 1; i < arr.length; i++) {
            System.out.print(" ");
            System.out.print(arr[i]);
        }
        System.out.println();
    }
    
    private static void print(long... arr) {
        System.out.print(arr[0]);
        for (int i = 1; i < arr.length; i++) {
            System.out.print(" ");
            System.out.print(arr[i]);
        }
        System.out.println();
    }
    
    private static <T> void print(T... arr) {
        System.out.print(arr[0]);
        for (int i = 1; i < arr.length; i++) {
            System.out.print(" ");
            System.out.print(arr[i]);
        }
        System.out.println();
    }
    
    private static void read(Scanner scan, int[]... arrs) {
        int len = arrs[0].length;
        for (int i = 0; i < len; i++) {
            for (int[] arr : arrs) {
                arr[i] = scan.nextInt();
            }
        }
    }
    
    private static void read(Scanner scan, long[]... arrs) {
        int len = arrs[0].length;
        for (int i = 0; i < len; i++) {
            for (long[] arr : arrs) {
                arr[i] = scan.nextLong();
            }
        }
    }
    
    private static void decreaseByOne(int[]... arrs) {
        for (int[] arr : arrs) {
            for (int i = 0; i < arr.length; i++) {
                arr[i] --;
            }
        }
    }
}