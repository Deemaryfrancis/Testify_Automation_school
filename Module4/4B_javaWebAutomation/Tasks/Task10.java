package Tasks;

import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.chrome.ChromeDriver;

public class Task10 {
    public static void main(String[] args) throws InterruptedException {
        System.setProperty("webdriver.chrome.driver", "C:\\Users\\odunuga\\kehinde-testify\\SeleniumWeb\\src\\chromedriver.exe");

        //Launch browser
        WebDriver driver = new ChromeDriver();

        //Maximize the browser
        driver.manage().window().maximize();

        //Navigate to the url
        driver.get("https://jqueryui.com/");
        driver.findElement(By.xpath("//a[contains(text(),'Dialog')]")).click();
        Thread.sleep(2000);
        driver.switchTo().frame(0);
        driver.findElement(By.cssSelector("span[class$='closethick']")).click();

        driver.close();
    }
}
