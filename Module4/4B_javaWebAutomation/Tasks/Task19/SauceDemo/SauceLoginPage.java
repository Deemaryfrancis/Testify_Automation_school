package pageObjectModel;

import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.support.FindBy;
import org.openqa.selenium.support.PageFactory;
import org.openqa.selenium.support.ui.WebDriverWait;

public class SauceLoginPage {
    WebDriver Sdriver=null;
    public SauceLoginPage(WebDriver driver){
        Sdriver = driver;
        PageFactory.initElements(Sdriver, this);
    }

    @FindBy (xpath = "//input[@id='user-name']")
    private WebElement username;
    public WebElement getUsername(){
        return username;
    }

    @FindBy (xpath = "//input[@id='password']")
    private WebElement password;
    public WebElement getPassword(){
        return password;
    }

    @FindBy (xpath = "//input[@id='login-button']")
    private WebElement login;

    public WebElement getLogin(){
        return login;
    }
}
