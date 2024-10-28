// PredictionForm.jsx
import React, { useState } from "react";
import axios from "axios";

const PredictionForm = () => {
  const [formData, setFormData] = useState({
    area: "",
    bedrooms: "",
    bathrooms: "",
    stories: "",
    mainroad: "yes",
    guestroom: "no",
    basement: "no",
    hotwaterheating: "no",
    airconditioning: "yes",
    parking: "",
    prefarea: "yes",
    furnishingstatus: "furnished",
  });
  const [prediction, setPrediction] = useState(null);

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData((prevState) => ({
      ...prevState,
      [name]: value,
    }));
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const response = await axios.post(
        "http://localhost:5000/predict",
        formData
      );
      setPrediction(response.data.predicted_price);
    } catch (error) {
      console.error("Erreur lors de la prédiction:", error);
    }
  };

  const renderInput = (name, label, type = "number") => (
    <div className="mb-4 md:mr-4">
      <label
        className="block text-dark font-normal text-sm mb-2"
        htmlFor={name}
      >
        {label}
      </label>
      <input
        className="appearance-none border border-slate-500 rounded w-full py-2 px-3 text-dark bg-none leading-tight focus:outline-none focus:shadow-outline"
        id={name}
        type={type}
        name={name}
        value={formData[name]}
        onChange={handleChange}
        required={type === "number"}
        min={type === "number" ? "0" : undefined}
      />
    </div>
  );

  const renderSelect = (name, label, options) => (
    <div className="mb-4 md:mr-4">
      <label
        className="block text-dark text-sm font-normal mb-2"
        htmlFor={name}
      >
        {label}
      </label>
      <select
        className="appearance-none border border-slate-500 rounded w-full py-2 px-3 text-dark bg-none leading-tight focus:outline-none focus:shadow-outline"
        id={name}
        name={name}
        value={formData[name]}
        onChange={handleChange}
      >
        {options.map((option) => (
          <option key={option} value={option.toLowerCase()}>
            {option}
          </option>
        ))}
      </select>
    </div>
  );

  return (
    <div className="flex flex-col items-center justify-center  w-full max-w-6xl px-4">
      <form
        onSubmit={handleSubmit}
        className="w-full bg-white shadow-md rounded-lg px-0 pt-6 pb-8 sm:px-8 "
      >
        <div className="flex -mx-4 gap-10">
          <div className="w-full md:w-1/2 px-4">
            <h3 className="w-full font-semibold text-lg text-dark mb-4">
              {" "}
              Champs basiques
            </h3>
            {renderInput("area", "Surface (en pieds carrés)")}
            {renderInput("bedrooms", "Nombre de chambres")}
            {renderInput("bathrooms", "Nombre de salles de bain")}
            {renderInput("stories", "Nombre d'étages")}
            {renderSelect("hotwaterheating", "Chauffage à eau chaude", [
              "Yes",
              "No",
            ])}
            {renderSelect("airconditioning", "Climatisation", ["Yes", "No"])}
          </div>
          <div className="max-h-full h-auto border border-slate-200"></div>
          <div className="w-full md:w-1/2 px-4">
            <h3 className="w-full font-semibold text-lg text-dark mb-4">
              {" "}
              Champs avancés
            </h3>

            {renderInput("parking", "Places de parking")}
            {renderSelect("mainroad", "Sur la route principale", ["Yes", "No"])}
            {renderSelect("guestroom", "Chambre d'amis", ["Yes", "No"])}
            {renderSelect("basement", "Sous-sol", ["Yes", "No"])}
            {renderSelect("prefarea", "Zone préférentielle", ["Yes", "No"])}
            {renderSelect("furnishingstatus", "État de l'ameublement", [
              "Furnished",
              "Semi-Furnished",
              "Unfurnished",
            ])}
          </div>
        </div>

        <div className="flex items-center justify-between mt-6">
          <button
            className="bg-accent hover:bg-accent hover:bg-opacity-80 text-white font-bold py-2 px-4 rounded focus:outline-none focus:shadow-outline hover:duration-200"
            type="submit"
          >
            Prédire le prix
          </button>
        </div>
      </form>
      {prediction && (
        <div
          className="w-full bg-accent/20 border-l-4 border-accent text-dark p-4 my-4"
          role="alert"
        >
          <p className="font-bold">Prix prédit :</p>
          <p>{prediction.toFixed(2)} $</p>
        </div>
      )}
    </div>
  );
};

export default PredictionForm;
