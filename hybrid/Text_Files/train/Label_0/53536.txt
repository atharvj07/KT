import java.util.*;

public class Rules {
  public static void main(String[] args) {
    Scanner in = new Scanner(System.in);
    int a = in.nextInt();
    double maxSpeed = in.nextInt();
    double len = in.nextInt();
    double delayDist = in.nextInt();
    double delaySpeed = in.nextInt();
    
    double timeToDelaySpeed = delaySpeed/a;
    double timeToDelay = travelS(a, 0.0, maxSpeed, delayDist);
    //System.out.printf("timeToDelaySpeed=%.5f, timeToDelay=%.5f\n", timeToDelaySpeed, timeToDelay);
    if (timeToDelay < timeToDelaySpeed) { // we won't reach delaySpeed before delay marker
      // 2 cases: we don't reach max by time we reach end
      timeToDelay = travelS(a, 0.0, maxSpeed, len);
      double timeToMax = maxSpeed/a;
      if (timeToDelay < timeToMax) {
        System.out.printf("%.9f\n", timeToDelay);
        return;
      }
      // we do reach max, then travel at max
      double[] parts = travelA(a, 0.0, maxSpeed);
      double remainingDist = len - parts[1];
      double time = parts[0] + remainingDist / maxSpeed;
      System.out.printf("%.9f\n", time);
      return;
    }
    if (delaySpeed > maxSpeed) {
      double time = travelS(a, 0.0, maxSpeed, len);
      System.out.printf("%.9f\n", time);
      return;
    }
    
    // binary search to find best velocity to stop acceleration in beginning
    double lowV = delaySpeed;
    double highV = maxSpeed;
    int loopCount = 1000;
    double[] initial = null;
    double[] secondary = null;
    while (loopCount-->0) {
      double guessV = (lowV+highV)/2.0;
      initial = travelA(a, 0.0, guessV);
      secondary = travelA(a, guessV, Math.min(delaySpeed, maxSpeed));
      if (initial[1] + secondary[1] < delayDist) { // okay, we can go faster
        lowV = guessV;
      } else {
        highV = guessV;
      }
    }
    double totalTime = 0.0;
    double finalSpeed = 0.0;
    initial = travelA(a, 0.0, lowV);
    secondary = travelA(a, lowV, delaySpeed);
    totalTime = initial[0] + secondary[0];
    double totalDist = initial[1] + secondary[1];
    totalTime += (delayDist-totalDist)/maxSpeed;
    
    // now we have delayDist to go, and we are at delaySpeed
    totalTime += travelS(a, delaySpeed, maxSpeed, len-delayDist);
    System.out.printf("%.9f\n", totalTime);
  }
  
  // [0] = time in h, [1] = dist travelled, in km
  // input units are in km/h^2, km/h, km/h
  public static double[] travelA(int a, double startSpeed, double endSpeed) {
    if (startSpeed > endSpeed)
      a = -a;
    
    double time = (endSpeed - startSpeed) / a;
    double dist = 0.5*a*time*time + startSpeed*time;
    return new double[] {time, dist};
  }
  
  // returns time it takes to travel dist, with given inputs
  public static double travelS(int a, double startSpeed, double maxSpeed, double dist) {
    double timeToMax = (maxSpeed - startSpeed) / a;
    double targetTime = (-startSpeed + Math.sqrt(startSpeed*startSpeed + 2*a*dist)) / a;
    if (targetTime < timeToMax)
      return targetTime;
    
    double partialDist = 0.5*timeToMax*timeToMax*a + startSpeed*timeToMax;
    double remainingDist = dist - partialDist;
    targetTime = remainingDist / maxSpeed;
    return targetTime + timeToMax;
  }
}