package com.treasurehunt;
import java.util.Random;
import java.util.Scanner;

public class TreasureHunt {
    public static void main(String[] args) {
        displayMap(0, 0);
    }

    public static void instructions(int maxAttempts) {
        System.out.println("You have "+maxAttempts+" attempts to find the treasure on a 5 x 5 map. \n" + //
                        "Enter a row from A to E and a column from 1 to 5. \n" + //
                        "Row letters may be entered in uppercase or lowercase. \n" + //
                        "The X marks your most recent guess.  \n" + //
                        "Invalid rows and columns do not use an attempt.  \n" + //
                        "\n" + //
                        "Direction clues tell you where the treasure is:\n" + //
                        "North, South, East, West, Northeast, Northwest, Southeast, or Southwest.\n" + //
                        "Rows run from A at the top to E at the bottom.  \n" + //
                        "Columns from 1 on the left to 5 on the right.  \n" + //
                        "\n" + //
                        "Distance counts horizontal and vertical steps, not diagonal steps. \n" + //
                        "Nearby: 1 step\n" + //
                        "Hot: 2 or 3 steps\n" + //
                        "Warm: 4 or 5 steps\n" + //
                        "Cold: 6 to 8 steps\n" + //
                        "");
    }

    public static int generateTreasureCoordinate() {
        Random random = new Random();
        return 1+random.nextInt(4);
    }

    public static boolean isValidRow(String row) {
        if (row.length()==1) {
            if ((row.charAt(0)<'f' && row.charAt(0)>='a') || (row.charAt(0)<'F' && row.charAt(0)>='A')) {
                return true;
            }
        }
        return false;
    }

    public static int readRow() {
        String row;
        Scanner input = new Scanner(System.in);
        System.out.println("Enter row (A-E):");
        row = input.nextLine();
        while (!isValidRow(row)) {
            System.out.println("Invalid row. Enter a letter from A to E:");
            row = input.nextLine();
        }
        input.close();
        return row.toLowerCase().charAt(0)-64;
    }

    public static char getRowLetter(int row) {
        return (char) ('@'+row);
    }

    public static boolean isValidCoordinate(int coordinate) {
        return coordinate<6 && coordinate>0;
    }

    public static int readColumn() {
        int column;
        Scanner input = new Scanner(System.in);
        System.out.println("Enter column (1-5):");
        column = input.nextInt();
        while (isValidCoordinate(column)) {
            System.out.println("Invalid row. Enter a letter from A to E:");
            column = input.nextInt();
        }
        input.close();
        return column;
    }

    public static boolean isTreasureFound(int treasureRow, int treasureColumn, int guessRow, int guessColumn) {
        return treasureColumn==guessColumn && treasureRow==guessRow;
    }

    public static String getVerticalDirection(int treasureRow, int guessRow) {
        if (treasureRow>guessRow) {
            return "South";
        }else if (treasureRow<guessRow) {
            return "North";
        }else {
            return "";
        }
    }

    public static String getHorizontalDirection(int treasureColumn, int guessColumn) {
        if (treasureColumn>guessColumn) {
            return "East";
        }else if (treasureColumn<guessColumn) {
            return "West";
        }else {
            return "";
        }
    }

    public static String getDirection(int treasureRow, int treasureColumn, int guessRow, int guessColumn) {
        String row=getVerticalDirection(treasureRow, guessRow);
        String column=getHorizontalDirection(treasureColumn, guessColumn);
        if (row.length()==0 || column.length()==0) {
            return row+column;
        } else {
            return row+column.toLowerCase();
        }
    }

    public static int calculateDifference(int first, int second) {
        int distance=first-second;
        if (distance<0) {
            return distance*-1;
        }
        return distance;
    }

    public static int calculateDistance(int treasureRow, int treasureColumn, int guessRow, int guessColumn) {
        return calculateDifference(guessRow, treasureRow)+calculateDifference(guessColumn, treasureColumn);
    }

    public static String getDistanceWord(int distance) {
        if (distance==0) {
            return "Found!";
        }else if (distance<2) {
            return "Nearby";
        }else if (distance<4) {
            return "Hot";
        }else if (distance<6) {
            return "Warm";
        }else {
            return "Cold";
        }
    }

    public static String getClue(int treasureRow, int treasureColumn, int guessRow, int guessColumn) {
        int distance = calculateDistance(treasureRow, treasureColumn, guessRow, guessColumn);
        String clue = getDistanceWord(distance);
        if (clue.equals("Found!")) {
            return clue;
        } else {
            String direction = getDirection(treasureRow, treasureColumn, guessRow, guessColumn);
            return "Direction: "+direction+"\nDistance : "+clue;
        }
    }

    public static void displayMapRow(int row, int guessRow, int guessColumn) {
        String out="";
        out+=getRowLetter(row)+"   |";
        for (int i = 0; i <5 ; i++) {
            if (guessRow==row && guessColumn==i+1) {
                out+=" X |";
            }else {
                out+="   |";
            }
        }
        System.out.println(out);
        System.out.println("    +---+---+---+---+---+");
    }

    public static void displayMap(int guessRow, int guessColumn) {
        System.out.println("");
        System.out.println("      1   2   3   4   5  ");
        System.out.println("    +---+---+---+---+---+");
        for (int i = 1; i < 6; i++) {
            displayMapRow(i, guessRow, guessColumn);
        }
        System.out.println("");
    }

    public static void playRound(int treasureRow, int treasureColumn, int maxAttempts) {
        Scanner input = new Scanner(System.in);
        displayMap(0, 0);
        boolean win=false;
        for (int i = 0; i < maxAttempts; i++) {
            System.out.println("Attempt #"+i+1);
            int row=readRow();
            int column=readColumn();
            displayMap(row, column);
            String clue = getClue(treasureRow, treasureColumn, row, column);
            if (clue.equals("Found!")) {
                System.out.println("Congratulations! You found the treasure!");
                i=maxAttempts;
                win=true;
            } else {
                System.out.println(clue);
            }
        }
        if (!win) {
            System.out.println("You ran out of attempts.\n" + //
                                "The treasure was at row "+treasureRow+", column "+treasureColumn+".\n" + //
                                "GAME OVER!!!");
        }
        System.out.println("Thanks for playing!");
    }

    public static int readMaxAttempts() {
        Scanner input = new Scanner(System.in);
        System.out.println("Enter the number of attempts the player has: ");
        int maxAttempts = input.nextInt();
        while (maxAttempts<1) {
            System.out.println("The number of attempts must be positive. Try again: ");
            maxAttempts = input.nextInt();
        }
        input.close();
        return maxAttempts;
    }

    public static void runGame() {
        int maxAttempts = readMaxAttempts();
        int treasureRow = generateTreasureCoordinate();
        int treasureColumn = generateTreasureCoordinate();
        playRound(treasureRow, treasureColumn, maxAttempts);
    }
}