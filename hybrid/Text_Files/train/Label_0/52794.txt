import java.util.Scanner;

class Card {
    String suit;
    int value;

    @Override
    public String toString() {
        return this.suit + this.value;
    }

    Card(String str) {
        this.suit = str.substring(0, 1);
        this.value = Integer.parseInt(str.substring(1));
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        Card[] arrOrigin = new Card[n];
        for (int i = 0; i < n; i++) {
            arrOrigin[i] = new Card(sc.next());
        }
        Card[] arrBubble = arrOrigin.clone();
        bubbleSort(arrBubble);
        printArray(arrBubble);
        System.out.println(isStable(arrOrigin, arrBubble) ? "Stable" : "Not stable");
        Card[] arrSelection = arrOrigin.clone();
        selectionSort(arrSelection);
        printArray(arrSelection);
        System.out.println(isStable(arrOrigin, arrSelection) ? "Stable" : "Not stable");
    }


    static boolean isStable(Card[] org, Card[] dst) {
        int orgN = org.length;
        int dstN = dst.length;
        boolean res = true;
        for (int i = 0; i < orgN; i++) {
            for (int j = i + 1; j < orgN; j++) {
                for (int a = 0; a < dstN; a++) {
                    for (int b = a + 1; b < dstN; b++) {
                        if (org[i].value == org[j].value && org[i] == dst[b] && org[j] == dst[a]) {
                           res = false;
                        }
                    }
                }
            }
        }
        return res;
    }


    static void bubbleSort(Card[] arr) {
        int n = arr.length;
        for (int i = 0; i < n; i++) {
            for (int j = n - 1; j > i; j--) {
                if (arr[j].value < arr[j - 1].value) {
                    Card tmp = arr[j];
                    arr[j] = arr[j - 1];
                    arr[j - 1] = tmp;
                }
            }
        }
    }

    static void selectionSort(Card[] arr) {
        int n = arr.length;
        for (int i = 0; i < n; i++) {
            int minJ = i;
            for (int j = i; j < n; j++) {
                if (arr[j].value < arr[minJ].value) {
                    minJ = j;
                }
            }
            Card tmp = arr[i];
            arr[i] = arr[minJ];
            arr[minJ] = tmp;
        }
    }


    static void printArray(Card[] arr) {
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < arr.length - 1; i++) {
            sb.append(arr[i]);
            sb.append(" ");
        }
        sb.append(arr[arr.length - 1]);
        System.out.println(sb.toString());
    }
}

