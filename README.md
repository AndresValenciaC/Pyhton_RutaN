<div align="center">
  <img src="https://i.postimg.cc/FFSRDrCJ/Imagen3.jpg" alt="Imagen3.jpg">
</div>


## Introduction


Welcome to an extraordinary journey into the realms of space exploration! Our project, in collaboration with Softserve, delves into the vast mysteries of the cosmos, pushing the boundaries of human knowledge and technology.

In the pursuit of unraveling the secrets of the universe, we specialize in the generation of advanced simulations and the creation of comprehensive mission reports for space exploration endeavors. These simulations, powered by cutting-edge technology, replicate various aspects of space missions, allowing us to analyze and anticipate challenges that astronauts and spacecraft may encounter.

### Table of Contents

- [Installation](#installation)
- [Configurations](#configurations)
- [Testing](#testing)
- [Next Steps](#next-steps)
- [Contributions](#contributions)
- [Roadmap](#roadmap)
- [Creators](#creators)
- [Sponsors](#sponsors)
- [License](#license)
- [Thanks](#thanks)

## Installation

Clone the project

```bash
  git clone https://github.com/AndresValenciaC/Pyhton_RutaN.git
```

Go to the project directory

```bash
  cd Pyhton_RutaN
```

Install dependencies

```bash
  poetry install
```

Activate the virtual environment

```bash
  poetry shell
```

Run the program

```bash
  python main.py
```

## Configurations

You can customize the configuration settings in two ways:

### Option 1: Modify `config.yaml`

1. Open the `config.yaml` file located in the project's root directory.

2. Locate the relevant configuration section you want to modify, which may include `numfiles_initicial`, `numfiles_final`, `time_cycle`, `status`, `missions`, `devices`, `date_format`, and others.

3. Update the necessary parameters according to your requirements.

4. Save the changes to the `config.yaml` file.

### Option 2: Use argparse

Alternatively, you can change specific configurations using command-line arguments with argparse. Here are the variables you can use:

- `--numfiles_initicial`: Specify the initial number of files.
- `--numfiles_final`: Specify the final number of files.
- `--time_cycle`: Specify the time cycle.

Example:

```bash
python main.py --numfiles_initicial 10 --numfiles_final 20 --time_cycle 5
```
## Testing

To ensure the reliability and quality of the project, thorough unit testing is employed. Here are the key unit test files:

[Files Generation](/tests/test_files_generation.py)  
[Reports](/tests/test_reports_file.py)  
[Backup](/tests/test_backup_file.py)  


These unit tests validate individual components and functions, ensuring they perform as expected. The test suite achieves a test coverage of over 60%, demonstrating a comprehensive examination of the codebase.

For more details on running these tests locally or contributing to the testing process, refer to the [Contributions](#contributions) section.

## Next Steps

The project is currently in its early stages, focusing on fundamental functionality through the command line interface. As it evolves, there are plans to introduce a user interface to enhance the overall user experience.

### Current Phase

In its current phase, the project has established essential functionality accessible through command-line operations.

### Upcoming Enhancements

As part of the next steps, the intention is to implement a graphical user interface, providing a more intuitive and user-friendly experience. This will enable a simpler and visually engaging interaction with the project's features.

## Contributions

Community contributions are encouraged to enhance and expand the project. Whether you have ideas, suggestions, or a desire to participate in development, your involvement is welcome!.

> **Note:**
> This project is in a continuous state of evolution, with upcoming enhancements dedicated to providing a more comprehensive and user-friendly experience.


Thank you for your interest and collaboration in advancing this project.

## Roadmap

### Version 1.1 (Next Release)

- [ ] Implement feature A to enhance functionality.
- [ ] Address user-reported bugs and issues.
- [ ] Optimize codebase for improved performance.

### Version 1.2

- [ ] Introduce a user-friendly graphical user interface (GUI).
- [ ] Add support for multiple languages.
- [ ] Enhance documentation with more detailed usage examples.

### Version 2.0 (Major Update)

- [ ] Integrate advanced analytics and reporting features.
- [ ] Explore compatibility with additional platforms.
- [ ] Conduct usability testing for further improvements.

### Future Considerations

- [ ] Explore potential integrations with third-party services.
- [ ] Enhance accessibility features for a broader user base.
- [ ] Gather user feedback for continuous improvement.

Feel free to contribute to discussions and provide feedback on the Feedback section to influence the roadmap!


## Creators

Feel free to reach out to us if you have any questions or feedback. We value your input! Here are the channels for contacting the creators:

<span style="width: 35px; display: inline-block;"></span>
<a href="https://www.rutanmedellin.org/" target="_blank">
  <img src="https://i.postimg.cc/Qds7Z9K7/unnamed.png" style="width: 90px; height: auto;">
</a>
<span style="width: 60px; display: inline-block;"></span>
<a href="https://www.rutanmedellin.org/" target="_blank">
  <img src="https://i.postimg.cc/Qds7Z9K7/unnamed.png" style="width: 90px; height: auto;">
</a>
<span style="width: 48px; display: inline-block;"></span>
<a href="https://www.rutanmedellin.org/" target="_blank">
  <img src="https://i.postimg.cc/Qds7Z9K7/unnamed.png" style="width: 90px; height: auto;">
</a>

 ~  " [Andrés Valencia](https://www.linkedin.com/in/juan-felipe-prada-suarez/) "   ~   " [Miguel Mulcue](https://www.linkedin.com/in/miguel-mulcue/) "   ~  " [ Juan Prada ](https://www.linkedin.com/in/juan-felipe-prada-suarez/) " ~ 


## Sponsors

Support this project by becoming a sponsor. Your logo will show up here with a link to your website.

<div style="text-align: center;">
<a href="https://www.softserveinc.com/en-us" target="_blank"><img src="data:image/jpeg;base64,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" style="width: 50px; height: auto;">
</a> 
<span style="width: 20px; display: inline-block;"></span>
<a href="https://www.rutanmedellin.org/" target="_blank">
  <img src="https://info.rutanmedellin.org/hubfs/Landing%20ruta%20n/VentaEspacios/thumbnail_pagina.png" style="width: 50px; height: auto;">
</a>
</div>

## License

This Proyect is [licensed](./LICENSE).

This Proyect documentation (e.g., `.md` files in the `/docs` folder) is [Team 32 licensed](./LICENSE-docs).

## Thanks

[Luis Vásquez - Teacher](https://www.linkedin.com/in/luisvasv/)

[Sebástian Eusse - Monitor](https://www.linkedin.com/in/sebastian-eusse/)

[CodingUpMyFuture - Bootcamp](https://github.com/codingupmyfuture)