import java.math.BigInteger;
import java.util.*;


public class LeetCode {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n, m, k;
        n = sc.nextInt(); //kol zelii
        m = sc.nextInt(); //kol zakl 1
        k = sc.nextInt(); //kol zakl 2
        int x, s;
        x = sc.nextInt(); //time to make 1
        s = sc.nextInt(); //mana size
        int[] xPower = new int[m+1];
        int[] xCost = new int[m+1];
        for (int i = 0;i < m; i++) {
            xPower[i] = sc.nextInt();
        }
        for (int i = 0;i < m; i++) {
            xCost[i] = sc.nextInt();
        }
        xPower[m] = x; xCost[m] = 0;
        m++;

        int[] kPower = new int[k];
        int[] kCost = new int[k];
        for (int i = 0; i < k; i++) {
            kPower[i] = sc.nextInt();
        }
        for (int i = 0; i < k; i++) {
            kCost[i] = sc.nextInt();
        }
        if (kPower.length > 0) {
            PowerAndCost powerAndCost = dropUseless(kPower, kCost);
            kPower = powerAndCost.power;
            kCost = powerAndCost.cost;
        }
        BigInteger answer = new BigInteger("100000000000000000000000000000000000000000000000000000");
        for (int i = 0; i < m; i++) {
            int currentN = n;
            int currentMana = s;
            int currentX = x;
            if (xCost[i] <= currentMana) {
                currentX = xPower[i];
                currentMana -= xCost[i];
            }
            int bestKIndex = Arrays.binarySearch(kCost, currentMana);
            if (bestKIndex >= 0) { //keyFound
                currentN -= kPower[bestKIndex];
            } else {
                bestKIndex = Math.abs(bestKIndex) - 2;
                if (bestKIndex >= 0) {
                    currentN -= kPower[bestKIndex];
                }
            }
            BigInteger newValue = new BigInteger(String.valueOf(currentN)).multiply(new BigInteger(String.valueOf(currentX)));
            if (answer.compareTo(newValue) == 1) {
                answer = newValue;
            }
        }
        System.out.println(answer);
    }

    private static PowerAndCost dropUseless(int[] power, int[] cost) {
        ArrayList<Integer> powerNew = new ArrayList<>();
        ArrayList<Integer> costNew = new ArrayList<>();
        PowerAndCost PowerAndCost = new PowerAndCost();
        if (power.length > 0) {
            int currentPower = power[0];
            int currentCost = cost[0];
            for (int i = 0; i < power.length; i++) {
                if (cost[i] == currentCost) {
                    if (currentPower < power[i]) {
                        currentPower = power[i];
                    }
                } else {
                    powerNew.add(currentPower);
                    costNew.add(currentCost);
                    currentPower = power[i];
                    currentCost = cost[i];
                }
            }
            powerNew.add(currentPower);
            costNew.add(currentCost);
        }
        PowerAndCost.power = powerNew.stream().mapToInt(i->i).toArray();
        PowerAndCost.cost = costNew.stream().mapToInt(i->i).toArray();
        return PowerAndCost;
    }
    private static class PowerAndCost {
        int[] power;
        int[] cost;
    }
}
