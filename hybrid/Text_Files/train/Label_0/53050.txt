import java.util.Scanner;

public class IQ {

    public static void main(String[] args) {
        int[] array = new int[4];
        try {
            Scanner in = new Scanner(System.in); // Import java.util.Scanner for
                                                    // it
            for (int j = 0; j < array.length; j++) {
                int k = in.nextInt();
                array[j] = k;
            }
        } catch (Exception e) {
            e.printStackTrace();
        }

        int result = 42;
        int a = array[3] - array[2];
        float b = ((float) array[3]) / ((float) array[2]);
        float bInt = (float) (array[3] / array[2]);
        float b1 = ((float) array[1]) / ((float) array[0]);
        float b2 = ((float) array[2]) / ((float) array[1]);
        if ((array[2] - array[1]) == a && (array[1] - array[0]) == a) {
            result = array[3] + a;
        } else if (b == b1 && b == b2) {
            float result1 = (int) ((float) array[3] * b);
            float result2 = ((float) array[3] * b);
            if ((result2 - result1) < 0.00001 && (result2 - result1) > -0.00001) {
                result = (int) ((float) array[3] * b);
            }
        }
        if (result == 0) {
            result = 42;
        }
        System.out.println(result);

    }

}