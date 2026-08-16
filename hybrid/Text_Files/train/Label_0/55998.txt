import java.util.Arrays;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        String input = sc.next();
        char[] result = new char[n];
        //SS
        Arrays.fill(result, 'S');
        if (input.charAt(0) == 'o')
            result[1] = 'S';
        else
            result[1] = 'W';
        for (int i = 1; i < n; i++) {
            if (result[i] == 'S') {
                if (input.charAt(i) == 'o') {
                    if (result[i - 1] == 'S')
                        result[(i + 1) % n] = 'S';
                    else
                        result[(i + 1) % n] = 'W';
                } else {
                    if (result[i - 1] == 'S')
                        result[(i + 1) % n] = 'W';
                    else
                        result[(i + 1) % n] = 'S';
                }
            } else {
                if (input.charAt(i) == 'o') {
                    if (result[i - 1] == 'S')
                        result[(i + 1) % n] = 'W';
                    else
                        result[(i + 1) % n] = 'S';
                } else {
                    if (result[i - 1] == 'S')
                        result[(i + 1) % n] = 'S';
                    else
                        result[(i + 1) % n] = 'W';
                }
            }
        }
        if(result[0] == 'S' && result[n - 1] == 'S'){
            StringBuilder res = new StringBuilder();
            res.append(result);
            System.out.println(res.toString());
            return;
        }
        //WS
        Arrays.fill(result, 'S');
        result[n - 1] = 'W';
        if (input.charAt(0) == 'o')
            result[1] = 'W';
        else
            result[1] = 'S';
        for (int i = 1; i < n; i++) {
            if (result[i] == 'S') {
                if (input.charAt(i) == 'o') {
                    if (result[i - 1] == 'S')
                        result[(i + 1) % n] = 'S';
                    else
                        result[(i + 1) % n] = 'W';
                } else {
                    if (result[i - 1] == 'S')
                        result[(i + 1) % n] = 'W';
                    else
                        result[(i + 1) % n] = 'S';
                }
            } else {
                if (input.charAt(i) == 'o') {
                    if (result[i - 1] == 'S')
                        result[(i + 1) % n] = 'W';
                    else
                        result[(i + 1) % n] = 'S';
                } else {
                    if (result[i - 1] == 'S')
                        result[(i + 1) % n] = 'S';
                    else
                        result[(i + 1) % n] = 'W';
                }
            }
        }
        if(result[0] == 'S' && result[n - 1] == 'W'){
            StringBuilder res = new StringBuilder();
            res.append(result);
            System.out.println(res.toString());
            return;
        }
        //SW
        Arrays.fill(result, 'S');
        result[0] = 'W';
        if (input.charAt(0) == 'o')
            result[1] = 'W';
        else
            result[1] = 'S';
        for (int i = 1; i < n; i++) {
            if (result[i] == 'S') {
                if (input.charAt(i) == 'o') {
                    if (result[i - 1] == 'S')
                        result[(i + 1) % n] = 'S';
                    else
                        result[(i + 1) % n] = 'W';
                } else {
                    if (result[i - 1] == 'S')
                        result[(i + 1) % n] = 'W';
                    else
                        result[(i + 1) % n] = 'S';
                }
            } else {
                if (input.charAt(i) == 'o') {
                    if (result[i - 1] == 'S')
                        result[(i + 1) % n] = 'W';
                    else
                        result[(i + 1) % n] = 'S';
                } else {
                    if (result[i - 1] == 'S')
                        result[(i + 1) % n] = 'S';
                    else
                        result[(i + 1) % n] = 'W';
                }
            }
        }
        if(result[0] == 'W' && result[n - 1] == 'S'){
            StringBuilder res = new StringBuilder();
            res.append(result);
            System.out.println(res.toString());
            return;
        }
        //WW
        Arrays.fill(result, 'S');
        result[0] = 'W';
        result[n - 1] = 'W';
        if (input.charAt(0) == 'o')
            result[1] = 'S';
        else
            result[1] = 'W';
        for (int i = 1; i < n; i++) {
            if (result[i] == 'S') {
                if (input.charAt(i) == 'o') {
                    if (result[i - 1] == 'S')
                        result[(i + 1) % n] = 'S';
                    else
                        result[(i + 1) % n] = 'W';
                } else {
                    if (result[i - 1] == 'S')
                        result[(i + 1) % n] = 'W';
                    else
                        result[(i + 1) % n] = 'S';
                }
            } else {
                if (input.charAt(i) == 'o') {
                    if (result[i - 1] == 'S')
                        result[(i + 1) % n] = 'W';
                    else
                        result[(i + 1) % n] = 'S';
                } else {
                    if (result[i - 1] == 'S')
                        result[(i + 1) % n] = 'S';
                    else
                        result[(i + 1) % n] = 'W';
                }
            }
        }
        if(result[0] == 'W' && result[n - 1] == 'W'){
            StringBuilder res = new StringBuilder();
            res.append(result);
            System.out.println(res.toString());
            return;
        }
        System.out.println(-1);
    }
}
