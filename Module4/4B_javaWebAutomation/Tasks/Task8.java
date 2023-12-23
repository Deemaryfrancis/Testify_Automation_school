package Tasks;

import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.chrome.ChromeDriver;

public class Task8 {
    public static void main(String[] args) throws InterruptedException {
        System.setProperty("webdriver.chrome.driver", "C:\\Users\\odunuga\\kehinde-testify\\SeleniumWeb\\src\\chromedriver.exe");

        //Launch browser
        WebDriver driver = new ChromeDriver();

        //Maximize the browser
        driver.manage().window().maximize();

        //Navigate to the url
        driver.get("https://idorenyinankoh.github.io/loginPage/");
        boolean blankState = driver.findElement(By.cssSelector("button#create")).isEnabled();
        System.out.println(blankState);
        driver.findElement(By.id("firstName")).sendKeys("Testify");
        driver.findElement(By.id("lastName")).sendKeys("Academy");
        driver.findElement(By.id("email")).sendKeys("user@testify.com");
        driver.findElement(By.id("password")).sendKeys("Testify");
        driver.findElement(By.id("confirmPass")).sendKeys("Testify");
        driver.findElement(By.name("xpLevel")).sendKeys("I am a software test engineer");
        driver.findElement(By.xpath("//input[@id='male']")).click();
        Thread.sleep(2000);
        boolean fillState = driver.findElement(By.cssSelector("button#create")).isEnabled();
        System.out.println(fillState);

        driver.close();
    }
}
