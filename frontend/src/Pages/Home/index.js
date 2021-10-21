import React, { useState, useRef } from "react";
//import Navbar from '../../Components/Navbar';
import { Page, Input, Image, Button, InputDiv, ImageDiv, P } from "./Style";
import placeholderImage from "../../Assets/Images/placeholder.png";
import axios from "axios";

const Home = () => {
  const [baseImage, setBaseImage] = useState();
  const fileTest = useRef(null);

  const convertBase64 = (file) =>
    new Promise((resolve, reject) => {
      const fileReader = new FileReader();
      fileReader.readAsDataURL(file);

      fileReader.onload = () => {
        resolve(fileReader.result);
      };

      fileReader.onerror = (error) => {
        reject(error);
      };
    });

  const uploadImage = async (e) => {
    const file = e?.target?.files[0];
    if (file) {
      const base64 = await convertBase64(file);
      setBaseImage(base64);
    }
  };

  return (
    <Page>
      {/* <Navbar /> */}
      <InputDiv>
        <P>
          C<small>la</small>S<small>sifier</small>GO
        </P>
        <ImageDiv>
          <Image
            src={baseImage ? baseImage : placeholderImage}
            height="500px"
            width="800px"
          />
        </ImageDiv>
        <Input
          accept="image/png, image/jpeg"
          type="file"
          ref={fileTest}
          onChange={(e) => uploadImage(e)}
        />
        <Button
          onClick={() => {
            axios
              .post("http://127.0.0.1:5000/image", {
                image: baseImage,
              })
              .then((r) => console.log(r));
          }}
        >
          Enviar
        </Button>
      </InputDiv>
    </Page>
  );
};

export default Home;
