
import { Wrapper, Content } from "./Header.styles";
import { Helmet } from "react-helmet";

const TITLE = "GlamourRizz";

const Header = () => {
    return (
        <>
            <Helmet>
                <title>{TITLE}</title>
            </Helmet>
            <header></header>
            <Wrapper>
                <Content>
                    <h1>GlamourRizz</h1>
                </Content>
            </Wrapper>
        </>
    );
};

export default Header;
