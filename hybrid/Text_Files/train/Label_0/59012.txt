import java.util.Scanner;

public class Solution {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String a = sc.next();
        String b = sc.next();

        int[] arr = new int[10];

        for (int i = 0; i < a.length(); i++) {
            arr[a.charAt(i) - '0']++;
        }

        if (a.length() < b.length()) {
            for (int i = arr.length - 1; i >= 0; i--) {
                for (int j = 0; j < arr[i]; j++) {
                    System.out.print(i);
                }
            }
        } else {
            int[] result = new int[a.length()];
            int c = 0;
            for (int i = 0; i < b.length(); i++) {
                if (arr[b.charAt(i) - '0'] > 0) {
                    result[c++] = b.charAt(i) - '0';
                    arr[b.charAt(i) - '0']--;
                } else {
                    break;
                }
            }
            if (c < result.length) {
                    for (int i = b.charAt(c) - '0'; i >= 0; i--) {
                        if (arr[i] > 0) {
                            result[c++] = i;
                            arr[i]--;
                            for (int k = arr.length - 1; k >= 0; k--) {
                                for (int j = 0; j < arr[k]; j++) {
                                    result[c++] = k;
                                }
                            }
                            break;
                        }
                    }
                    if (c < result.length) {
                        while (true) {
                            int o = result[c - 1] - 1;
                            for (int i = o; i >= 0; i--) {
                                if (arr[i] > 0) {
                                    arr[result[c - 1]]++;
                                    result[c - 1] = i;
                                    arr[i]--;
                                    for (int k = arr.length - 1; k >= 0; k--) {
                                        for (int j = 0; j < arr[k]; j++) {
                                            result[c++] = k;
                                        }
                                    }
                                    break;
                                }
                            }
                            if (c < result.length) {
                                arr[result[c - 1]]++;
                                c--;
                            } else {
                                break;
                            }
                        }
                    }
                System.out.println();
            }
            for (int i = 0; i < result.length; i++) {
                System.out.print(result[i]);
            }
        }
        System.out.println();
    }
}