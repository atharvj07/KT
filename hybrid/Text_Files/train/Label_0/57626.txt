import java.util.*;

/**
 * テ」ツつオテ」ツつ、テ」ツつウテ」ツδュテ」ツつ津ィツ。ツィテ」ツ?凖」ツつッテ」ツδゥテ」ツつケ
 */
class Dice{
  String t, s, e, n, w, b;

  /**
   * テ」ツつウテ」ツδウテ」ツつケテ」ツδ暗」ツδゥテ」ツつッテ」ツつソ
   * @param t テ、ツクツ甘ゥツ敖「
   * @param s テ・ツ債療ゥツ敖「
   * @param e テヲツ敖アテゥツ敖「
   * @param n テ・ツ個療ゥツ敖「
   * @param w ティツ・ツソテゥツ敖「
   * @param b テ、ツクツ凝ゥツ敖「
   */
  Dice(String t, String s, String e, String n, String w, String b){
    this.t = t;
    this.s = s;
    this.e = e;
    this.n = n;
    this.w = w;
    this.b = b;
  }

  /**
   * テ、ツクツ甘ゥツ敖「テ」ツ?古ヲツ敖アテゥツ敖「テ」ツ?ォテヲツ敖・テ」ツつ凝」ツつ暗」ツ??」ツ?ォテ・ツ崢榲ィツサツ「
   * @return テ・ツ崢榲ィツサツ「テ・ツセツ古」ツ?ョテ」ツつオテ」ツつ、テ」ツつウテ」ツδュ
   */
  public Dice moveEast(){
    return new Dice(w, s, t, n, b, e);
  }

  /**
   * テ、ツクツ甘ゥツ敖「テ」ツ?古・ツ個療ゥツ敖「テ」ツ?ォテヲツ敖・テ」ツつ凝」ツつ暗」ツ??」ツ?ォテ・ツ崢榲ィツサツ「
   * @return テ・ツ崢榲ィツサツ「テ・ツセツ古」ツ?ョテ」ツつオテ」ツつ、テ」ツつウテ」ツδュ
   */
  public Dice moveNorth(){
    return new Dice(s, b, e, t, w, n);
  }

  /**
   * テ・ツ個療ゥツ敖「テ」ツ?古ヲツ敖アテゥツ敖「テ」ツ?ォテヲツ敖・テ」ツつ凝」ツつ暗」ツ??」ツ?ォテ・ツ崢榲ィツサツ「
   * @return テ・ツ崢榲ィツサツ「テ・ツセツ古」ツ?ョテ」ツつオテ」ツつ、テ」ツつウテ」ツδュ
   */
  public Dice moveRight(){
    return new Dice(t, e, n, w, s, b);
  }

  /**
   * テ・ツシツ陛ヲツ閉ーテ」ツ?ォテヲツクツ。テ」ツ?陛」ツつ古」ツ?淌」ツつオテ」ツつ、テ」ツつウテ」ツδュテ」ツ?ィthisテ」ツ?古・ツ?ィテ」ツ?湘・ツ青古」ツ?佚」ツ?凝」ツ?ゥテ」ツ??」ツ?凝・ツ按、テ・ツョツ堙」ツ?凖」ツつ?
   * @param dice thisテ」ツ?ィテヲツッツ氾ィツシツε」ツ?療」ツ?淌」ツ??」ツつオテ」ツつ、テ」ツつウテ」ツδュ
   * @return テ・ツ?ィテ」ツ?湘・ツ青古」ツ?佚」ツ?ェテ」ツつ嘉」ツ?ーtrue, テ・ツ青古」ツ?佚」ツ?ァテ」ツ?ェテ」ツ??」ツ?ェテ」ツつ嘉」ツ?ーfalse
   */
  public boolean equals(Dice dice){
    return
      this.t.equals(dice.t) &&
      this.s.equals(dice.s) &&
      this.e.equals(dice.e) &&
      this.n.equals(dice.n) &&
      this.w.equals(dice.w) &&
      this.b.equals(dice.b);
  }

  /**
   * テ」ツδ湘」ツδε」ツつキテ」ツδ・テ・ツ?、テ」ツつ津ィツソツ氾」ツ??
   * @return テ」ツδ湘」ツδε」ツつキテ」ツδ・テ・ツ?、
   */
  public int hashCode(){
    return
      t.hashCode() +
      s.hashCode() +
      e.hashCode() +
      n.hashCode() +
      w.hashCode() +
      b.hashCode();
  }

  /**
   * テ」ツつオテ」ツつ、テ」ツつウテ」ツδュテ」ツつ津・ツ崢榲ィツサツ「テ」ツ?療」ツ?ヲテ・ツ?ィテ」ツ?ヲテ」ツ?ョテァツ環カテヲツ?凝」ツつ津ァツ板淌ヲツ按静」ツ?療」ツ?ヲティツソツ氾」ツ??
   * @return テ・ツ崢榲ィツサツ「テ・ツセツ古」ツ?ョテ・ツ?ィテ」ツ?ヲテ」ツ?ョテァツ環カテヲツ??
   */
  public ArrayList<Dice> getAllStates(){
    ArrayList<Dice> states = new ArrayList<Dice>();
    Dice dice = new Dice(t, s, e, n, w, b);

    for(int i = 0; i < 6; i++){
      for(int j = 0; j < 4; j++){
        states.add(dice);
        dice = dice.moveRight();
      }
      if(i < 4) dice = dice.moveNorth();
      if(i == 3) dice = dice.moveEast();
      if(i == 4) dice = dice.moveEast().moveEast();
    }

    return states;
  }
}

public class Main{
  public static void main(String[] args){
    Scanner sc = new Scanner(System.in);

    while(true){
      int n = sc.nextInt();
      if(n == 0) break;

      //テ」ツ?禿」ツ?ョテ」ツδェテ」ツつケテ」ツδ暗」ツ?ォテ・ツ?・テ」ツ?」テ」ツ?ヲテ」ツ??」ツつ凝」ツつオテ」ツつ、テ」ツつウテ」ツδュテ」ツ?ッテ」ツ??・ツ?ィテ」ツ?ヲテゥツ?陛」ツ??、ツスツ愿・ツ督?
      ArrayList<Dice> uniq = new ArrayList<Dice>();

      for(int i = 0; i < n; i++){
        String[] c = new String[6];

        for(int j = 0; j < 6; j++){
          c[j] = sc.next();
        }

        boolean addFlg = true;
        Dice d = new Dice(c[0], c[1], c[2], c[4], c[3], c[5]);
        ArrayList<Dice> states1 = d.getAllStates();

        for(Dice dice : uniq){
          ArrayList<Dice> states2 = dice.getAllStates();

          if(hasCommonDice(states1, states2)){
            addFlg = false;
            break;
          }
        }

        if(addFlg){
          uniq.add(d);
        }
      }

      System.out.println(n - uniq.size());
    }
  }

  /**
   * 2テ」ツ?、テ」ツ?ョテ」ツδェテ」ツつケテ」ツδ暗」ツ?ォテ・ツ?アテゥツ?堙」ツ?療」ツ?淌」ツつオテ」ツつ、テ」ツつウテ」ツδュテ」ツ?古」ツ?づ」ツつ凝」ツ?凝・ツ按、テ・ツョツ堙」ツ?凖」ツつ?
   * @param states1 テ」ツδェテ」ツつケテ」ツδ暗ッツシツ妥」ツ?、テァツ崢ョ
   * @param states2 テ」ツδェテ」ツつケテ」ツδ暗ッツシツ津」ツ?、テァツ崢ョ
   * @return true:テ・ツ?アテゥツ?堙」ツ?ョテ」ツ?陛」ツ??」ツ?禿」ツつ催」ツ?古」ツ?づ」ツつ? false:テ・ツ?アテゥツ?堙」ツ?ョテ」ツ?陛」ツ??」ツ?禿」ツつ催」ツ?古」ツ?ェテ」ツ??
   */
  public static boolean hasCommonDice(ArrayList<Dice> states1, ArrayList<Dice> states2){
    for(int i = 0; i < states1.size(); i++){
      for(int j = 0; j < states2.size(); j++){
        if(states1.get(i).equals(states2.get(j))){
          return true;
        }
      }
    }

    return false;
  }
}