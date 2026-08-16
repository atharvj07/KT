import java.util.*;

class Plant {
    private int length;
    private int glowthOfNobiro;
    private int glowthOfTidime;

    public Plant(int length, int glowthOfNobiro, int glowthOfTidime) {
        this.length = length;
        this.glowthOfNobiro = glowthOfNobiro;
        this.glowthOfTidime = glowthOfTidime;
    }

    public void growPlant(String message) {
        if (message.equals("nobiro")) {
            this.length += this.glowthOfNobiro;
            if (this.length < 0) {
                this.length = 0;
            }
        } else if (message.equals("tidime")) {
            this.length += this.glowthOfTidime;
            if (this.length < 0) {
                this.length = 0;
            }
        } else if (message.equals("karero")) {
            this.length = 0;
        }
    }

    public int getLength() {
        return this.length;
    }
}

public class Main {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int X = Integer.parseInt(sc.next());
        int A = Integer.parseInt(sc.next());
        int B = Integer.parseInt(sc.next());

        Plant plant = new Plant(X, A, B);

        int N = Integer.parseInt(sc.next());
        for (int i = 0; i < N; i++) {
            String S = sc.next();
            plant.growPlant(S);
        }

        System.out.println(plant.getLength());
    }
}


